from django.conf import settings
from django.contrib.auth import logout, login, authenticate
from django.core.mail import send_mail
from django.template.loader import get_template
from recommender.models import CustomUser
from recommender.serializers.user import UserSerializer, ForgotPasswordSerializer, RecoverPasswordSerializer, ChangePasswordSerializer, RegisterSerializer
from rest_framework import status, generics, mixins
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import NotAuthenticated
from rest_framework.permissions import AllowAny
from rest_framework.response import Response


class Login(generics.GenericAPIView):

    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        user = authenticate(username=request.data.get("username"), password=request.data.get("password"))
        if not user:
            return Response({"error": "Incorrect login"}, status=status.HTTP_401_UNAUTHORIZED)
        login(request, user)
        token = Token.objects.get(user=user)
        return Response({"token": token.key}, status=status.HTTP_200_OK)


class Logout(mixins.RetrieveModelMixin,
             generics.GenericAPIView):

    permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
        logout(request)
        return Response({"success": "User logged out successfully"}, status=status.HTTP_200_OK)


class User(mixins.RetrieveModelMixin,
                mixins.UpdateModelMixin,
                generics.GenericAPIView):

    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

    def get_object(self):
        if not self.request.user.is_authenticated():
            raise NotAuthenticated()
        return self.request.user

    def get_serializer_class(self):
        return UserSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class Register(mixins.CreateModelMixin,
                generics.GenericAPIView):

    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ChangePasswordView(mixins.UpdateModelMixin,
                            mixins.DestroyModelMixin,
                            generics.GenericAPIView):

    serializer_class = ChangePasswordSerializer

    def patch(self, request, *args, **kwargs):
        user = self.request.user
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            if not user.check_password(serializer.data.get("old_password")):
                return Response({"error": "Wrong password"}, status=status.HTTP_400_BAD_REQUEST)
            user.set_password(serializer.data.get("new_password"))
            user.save()
            return Response({"success":"Password changed"}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ForgotPassword(generics.GenericAPIView):

    permission_classes = (AllowAny,)
    serializer_class = ForgotPasswordSerializer

    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        if not email:
            return Response({"error":"Email not given"}, status=status.HTTP_400_BAD_REQUEST)
        user = CustomUser.objects.get(email=email)
        token = user.set_change_password_token()
        context = {
            'url': "?token=" + token + "&email=" + email,
        }
        html_message = get_template("email/forget_password.html").render(context)
        message = get_template("email/forget_password.txt").render(context)

        send_mail(
            subject='Did you forget your password?',
            message=message,
            from_email=settings.EMAIL_ADMIN,
            recipient_list=[email],
            html_message=html_message,
        )
        return Response({"success":"Email sent with token"}, status=status.HTTP_200_OK)


class RecoverPassword(generics.GenericAPIView):

    permission_classes = (AllowAny,)
    serializer_class = RecoverPasswordSerializer

    def post(self, request, *args, **kwargs):
        password = request.data.get('password')
        token = request.data.get('token')
        email = request.data.get('email')
        if not (token and password and email):
            return Response({"error":"Token, email or password not given"}, status=status.HTTP_400_BAD_REQUEST)
        user = CustomUser.objects.get(email=email)
        changed = user.change_password(token, password)
        if changed:
            return Response({"success":"Password changed"}, status=status.HTTP_200_OK)
        else:
            return Response({"error":"Password could not be changed. Please try again"}, status=status.HTTP_400_BAD_REQUEST)

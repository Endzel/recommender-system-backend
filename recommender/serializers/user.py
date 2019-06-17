from rest_framework import serializers

from recommender.models import CustomUser, UserContext, PreferenceGrade
from recommender.serializers.item import ItemAttributeSerializer
from recommender.serializers.context import ContextSegmentSerializer


class UserContextSerializer(serializers.ModelSerializer):

    context_segment = ContextSegmentSerializer()

    class Meta:
        model = UserContext
        fields = '__all__'


class PreferenceGradeSerializer(serializers.ModelSerializer):

    item_attribute = ItemAttributeSerializer()

    class Meta:
        model = PreferenceGrade
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):

    preference_grades = PreferenceGradeSerializer(required=False, many=True, allow_null=True)
    user_contexts = UserContextSerializer(required=False, many=True, allow_null=True)

    class Meta:
        model = CustomUser
        fields = ('id', 'first_name', 'last_name', 'birth_date', 'preference_grades', 'user_contexts')


class RegisterSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=False)
    birth_date = serializers.DateField(required=False)

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email', 'password', 'birth_date')


class ForgotPasswordSerializer(serializers.Serializer):

    email = serializers.EmailField(required=True)


class ChangePasswordSerializer(serializers.Serializer):

    new_password = serializers.CharField(required=True)
    old_password = serializers.CharField(required=True)


class RecoverPasswordSerializer(serializers.Serializer):

    password = serializers.CharField(required=True)
    token = serializers.CharField(required=True)

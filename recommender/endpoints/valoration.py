from recommender.models import Valoration
from recommender.serializers.valoration import ValorationSerializer
from rest_framework import generics, mixins


class ValorationView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):

    queryset = Valoration.objects.all()
    serializer_class = ValorationSerializer

    def get_queryset(self):
        return Valoration.objects.filter(user=self.request.user)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

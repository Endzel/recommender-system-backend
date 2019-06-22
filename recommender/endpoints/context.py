from recommender.models import ContextSegment, Implication
from recommender.serializers.context import ContextSegmentSerializer, ImplicationSerializer, ContextSegmentChoicesSerializer
from rest_framework import generics, mixins


class ContextSegmentView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):

    queryset = ContextSegment.objects.all()
    serializer_class = ContextSegmentSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ImplicationView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):

    queryset = Implication.objects.all()
    serializer_class = ImplicationSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ContextSegmentChoicesView(mixins.ListModelMixin, generics.GenericAPIView):

    queryset = ContextSegment.objects.all()
    serializer_class = ContextSegmentChoicesSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

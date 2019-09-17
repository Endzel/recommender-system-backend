from recommender.models import ContextSegment, UserContext, Implication, RecommendationContext
from recommender.serializers.context import ContextSegmentSerializer, UserContextSerializer, ImplicationSerializer, ContextSegmentChoicesSerializer, RecommendationContextSerializer
from rest_framework import generics, mixins


class ContextSegmentView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):

    queryset = ContextSegment.objects.all()
    serializer_class = ContextSegmentSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class UserContextView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):

    queryset = UserContext.objects.all()
    serializer_class = UserContextSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class RecommendationContextView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):

    queryset = RecommendationContext.objects.all()
    serializer_class = RecommendationContextSerializer

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

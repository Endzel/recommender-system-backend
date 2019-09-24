from recommender.models import Recommendation, Group
from recommender.serializers.recommendation import RecommendationSerializer, RecommendationCreateSerializer

from rest_framework import generics, mixins


class RecommendationView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):

    queryset = Recommendation.objects.all()
    serializer_class = RecommendationSerializer

    def get_queryset(self):
        g = Group.objects.filter(users__in=[self.request.user.id])
        return Recommendation.objects.filter(group__in=g)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.serializer_class = RecommendationCreateSerializer
        return self.create(request, *args, **kwargs)


class RecommendationSingleView(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, generics.GenericAPIView):

    queryset = Recommendation.objects.all()
    serializer_class = RecommendationSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        self.serializer_class = RecommendationCreateSerializer
        return self.update(request, *args, **kwargs)

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

    def get_queryset(self):
        context = self.request.GET.get('context', None)
        if context:
            q = UserContext.objects.filter(user=self.request.user, context_segment_id=context)
            if q:
                return q
        return []

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class UserContextSingleView(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):

    queryset = UserContext.objects.all()
    serializer_class = UserContextSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


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

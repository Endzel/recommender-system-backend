from recommender.models import Group
from recommender.serializers.group import GroupSerializer
from rest_framework import generics, mixins


class GroupView(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, generics.GenericAPIView):

    queryset = Group.objects.all()
    serializer_class = GroupSerializer

    def get_queryset(self):
        return Group.objects.filter(users__in=[self.request.user])

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

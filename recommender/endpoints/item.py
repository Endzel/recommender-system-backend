from recommender.models import Item, ItemAttribute, AttributeCategory, City, PertenanceGrade
from recommender.serializers.item import ItemSerializer, ItemAttributeSerializer, AttributeCategorySerializer, CitySerializer, CityChoicesSerializer, PertenanceGradeSerializer
from rest_framework import generics, mixins


class ItemView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):

    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ItemSingleView(mixins.RetrieveModelMixin, generics.GenericAPIView):

    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class ItemValoratedView(mixins.ListModelMixin, generics.GenericAPIView):

    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def get_queryset(self):
        return Item.objects.filter(valorations__user=self.request.user).distinct()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class ItemAttributeView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):

    queryset = ItemAttribute.objects.all()
    serializer_class = ItemAttributeSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class AttributeCategoryView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):

    queryset = AttributeCategory.objects.all()
    serializer_class = AttributeCategorySerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class PertenanceGradeView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):

    queryset = PertenanceGrade.objects.all()
    serializer_class = PertenanceGradeSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class CityView(mixins.ListModelMixin, generics.GenericAPIView):

    queryset = City.objects.all()
    serializer_class = CitySerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class CityChoicesView(mixins.ListModelMixin, generics.GenericAPIView):

    queryset = City.objects.all()
    serializer_class = CityChoicesSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

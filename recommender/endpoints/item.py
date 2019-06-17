from recommender.models import Item, ItemAttribute, AttributeCategory, City
from recommender.serializers.item import ItemSerializer, ItemAttributeSerializer, AttributeCategorySerializer, CitySerializer
from rest_framework import generics, mixins


class ItemView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):

    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


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


class CityView(mixins.ListModelMixin, generics.GenericAPIView):

    queryset = City.objects.all()
    serializer_class = CitySerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

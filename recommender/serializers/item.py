from rest_framework import serializers

from recommender.serializers.valoration import ValorationSerializer

from recommender.models import Item, ItemAttribute, AttributeCategory, City, PertenanceGrade, Valoration


class CitySerializer(serializers.ModelSerializer):

    class Meta:
        model = City
        fields = '__all__'


class ItemSerializer(serializers.ModelSerializer):

    city = CitySerializer(required=False)
    valoration = serializers.SerializerMethodField(required=False, method_name="get_my_valoration")

    class Meta:
        model = Item
        fields = '__all__'

    def get_my_valoration(self, obj):
        valoration = Valoration.objects.filter(user=self.context['request'].user, item=obj)
        if valoration.exists():
            return ValorationSerializer(valoration.first()).data
        return None


class ItemAttributeSerializer(serializers.ModelSerializer):

    class Meta:
        model = ItemAttribute
        fields = '__all__'


class AttributeCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = AttributeCategory
        fields = '__all__'


class PertenanceGradeSerializer(serializers.ModelSerializer):

    class Meta:
        model = PertenanceGrade
        fields = '__all__'


class CityChoicesSerializer(serializers.ModelSerializer):

    key = serializers.SerializerMethodField('get_id')
    text = serializers.SerializerMethodField('get_name')

    class Meta:
        model = City
        fields = ('key', 'text')

    def get_id(self, obj):
        return obj.id

    def get_name(self, obj):
        return obj.name

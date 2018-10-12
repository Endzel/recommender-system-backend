from rest_framework import serializers

from recommender.models import ItemType, Valoration



class ItemTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = ItemType
        fields = '__all__'


class ValorationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Valoration
        fields = '__all__'

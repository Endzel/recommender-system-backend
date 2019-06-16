from rest_framework import serializers

from recommender.models import ItemAttribute, Valoration



class ItemAttributeSerializer(serializers.ModelSerializer):

    class Meta:
        model = ItemAttribute
        fields = '__all__'


class ValorationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Valoration
        fields = '__all__'

from rest_framework import serializers

from recommender.models import Recommendation


class RecommendationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Recommendation
        fields = '__all__'


class ItemAttributeSerializer(serializers.ModelSerializer):

    class Meta:
        model = ItemAttribute
        fields = '__all__'


class AttributeCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = AttributeCategory
        fields = '__all__'


class CitySerializer(serializers.ModelSerializer):

    class Meta:
        model = City
        fields = '__all__'

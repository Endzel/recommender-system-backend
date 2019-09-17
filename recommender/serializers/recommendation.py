from rest_framework import serializers

from recommender.models import Recommendation
from recommender.serializers.item import ItemSerializer, CitySerializer
from recommender.serializers.group import RecommendationGroupSerializer


class RecommendationSerializer(serializers.ModelSerializer):

    group = RecommendationGroupSerializer(required=False)
    items = ItemSerializer(required=False, many=True)
    city = CitySerializer(required=False)

    class Meta:
        model = Recommendation
        fields = '__all__'


class RecommendationCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Recommendation
        fields = '__all__'

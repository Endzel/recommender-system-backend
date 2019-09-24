from rest_framework import serializers

from recommender.models import Recommendation, Valoration
from recommender.serializers.valoration import ValorationSerializer
from recommender.serializers.item import ItemSerializer, CitySerializer
from recommender.serializers.group import RecommendationGroupSerializer


class RecommendationSerializer(serializers.ModelSerializer):

    group = RecommendationGroupSerializer(required=False)
    items = ItemSerializer(required=False, many=True)
    city = CitySerializer(required=False)
    valoration = serializers.SerializerMethodField(required=False, method_name="get_my_valoration")

    class Meta:
        model = Recommendation
        fields = '__all__'

    def get_my_valoration(self, obj):
        valoration = Valoration.objects.filter(user=self.context['request'].user, recommendation=obj)
        if valoration.exists():
            return ValorationSerializer(valoration.first()).data
        return None


class RecommendationCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Recommendation
        fields = '__all__'

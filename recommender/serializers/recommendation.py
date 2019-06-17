from rest_framework import serializers

from recommender.models import Recommendation


class RecommendationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Recommendation
        fields = '__all__'

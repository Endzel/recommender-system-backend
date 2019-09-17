from rest_framework import serializers

from recommender.models import Group
from recommender.serializers.user import UserSerializer


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = '__all__'


class RecommendationGroupSerializer(serializers.ModelSerializer):

    users = UserSerializer(required=False, many=True)

    class Meta:
        model = Group
        fields = '__all__'

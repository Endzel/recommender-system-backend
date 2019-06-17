from rest_framework import serializers

from recommender.models import Group


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = '__all__'

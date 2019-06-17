from rest_framework import serializers

from recommender.models import Valoration


class ValorationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Valoration
        fields = '__all__'

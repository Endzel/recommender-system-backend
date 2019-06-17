from rest_framework import serializers

from recommender.models import ContextSegment, Implication


class ContextSegmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = ContextSegment
        fields = '__all__'


class ImplicationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Implication
        fields = '__all__'

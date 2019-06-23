from rest_framework import serializers

from recommender.models import ContextSegment, UserContext, Implication


class ContextSegmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = ContextSegment
        fields = '__all__'


class UserContextSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserContext
        fields = '__all__'


class ImplicationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Implication
        fields = '__all__'


class ContextSegmentChoicesSerializer(serializers.ModelSerializer):

    key = serializers.SerializerMethodField('get_id')
    text = serializers.SerializerMethodField('get_domain')

    class Meta:
        model = ContextSegment
        fields = ('key', 'text')

    def get_id(self, obj):
        return obj.id

    def get_domain(self, obj):
        return obj.domain

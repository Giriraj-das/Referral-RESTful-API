from rest_framework import serializers

from ref_codes.models import RefCode


class RefCodeCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = RefCode
        fields = '__all__'


class RefCodeDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = RefCode
        fields = ('id',)
import secrets
from rest_framework import serializers
from ref_codes.models import RefCode
from users.models import User


class RefCodeCreateSerializer(serializers.ModelSerializer):
    valid_to = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')

    class Meta:
        model = RefCode
        fields = '__all__'

    def create(self, validated_data):
        auth_user_id = self.context['request'].user.id

        ref_code = RefCode.objects.create(
            code=secrets.token_urlsafe(6),
            is_active=True,
            valid_to=validated_data.get('valid_to'),
            user_id=auth_user_id
        )
        return ref_code


class RefCodeDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = RefCode
        fields = ('id',)


class GetRefCodeByEmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = RefCode
        fields = ('code',)


class SwaggerRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = RefCode
        fields = ('valid_to',)


class SwaggerRequestEmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email',)


class DummyDetailSerializer(serializers.Serializer):
    detail = serializers.CharField()

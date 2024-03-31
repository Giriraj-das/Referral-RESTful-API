from rest_framework import serializers

from ref_codes.models import RefCode
from users.models import User


class UserListSerializer(serializers.ModelSerializer):
    date_joined = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')
    total_referrals = serializers.IntegerField(read_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'date_joined', 'total_referrals')


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        exclude = ('date_joined', 'last_login')

    def create(self, validated_data):
        user = super().create(validated_data)
        print(validated_data.get('password'))
        user.set_password(validated_data['password'])
        user.save()
        return user


class UserCreateReferralSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        exclude = ('date_joined', 'last_login')

    def validate(self, attrs):
        code = self.context['request'].parser_context['kwargs']['code']

        ref_code_obj = RefCode.objects.filter(code=code, is_active=True).first()
        if not ref_code_obj:
            raise serializers.ValidationError('Invalid or inactive referral code')
        if not ref_code_obj.is_valid():
            raise serializers.ValidationError('Referral code has expired')

        attrs['referer_user_id'] = ref_code_obj.user_id

        return attrs

    def create(self, validated_data):
        user = super().create(validated_data)
        print(validated_data.get('password'))
        user.set_password(validated_data['password'])
        user.save()
        return user


class UserDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id',)


class SwaggerCreateRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'first_name', 'last_name', 'email')


class DummyDetailSerializer(serializers.Serializer):
    detail = serializers.CharField()

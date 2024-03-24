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

    def validate(self, attrs):
        code = self.context['view'].kwargs.get('code')

        ref_code_obj = RefCode.objects.filter(code=code, is_active=True).first()
        if not ref_code_obj:
            raise serializers.ValidationError('Invalid or inactive referral code')
        if not ref_code_obj.is_valid():
            raise serializers.ValidationError('Referral code has expired')

        attrs['referer_user_id'] = ref_code_obj.user_id

        return attrs

    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user


class UserDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id',)

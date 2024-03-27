from django.db.models import Count
from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework import status
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from users.models import User
from users.permissions import UserDeletePermission
from users.serializers import UserListSerializer, UserCreateSerializer, UserDestroySerializer, \
    SwaggerCreateRequestSerializer, DummyDetailSerializer


class UserListView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer

    @extend_schema(
        summary='Get all users; or get referrals by referrer id',
        description='Not enter the "ref_id" - list of users with a count of the number of referrals. \
        Enter the "ref_id" - list of referrals by referrer id.',
        responses={
            status.HTTP_200_OK: UserListSerializer,
            status.HTTP_400_BAD_REQUEST: DummyDetailSerializer,
            status.HTTP_404_NOT_FOUND: DummyDetailSerializer,
            status.HTTP_500_INTERNAL_SERVER_ERROR: DummyDetailSerializer,
        },
        parameters=[
            OpenApiParameter(
                name='ref_id',
                location=OpenApiParameter.QUERY,
                description='If you want get referrals by referrer',
                required=False,
                type=int
            ),
        ]
    )
    def get(self, request, *args, **kwargs):
        ref_id = request.GET.get('ref_id', None)
        if ref_id:
            self.queryset = self.queryset.filter(referer_user_id=ref_id)
        else:
            self.queryset = self.queryset.annotate(total_referrals=Count('user'))

        return super().get(request, *args, **kwargs)


class UserCreateView(CreateAPIView):
    model = User.objects.all()
    serializer_class = UserCreateSerializer

    @extend_schema(
        summary='Create user. Create user with referral code.',
        description='Not enter the "code" - usually a user is created. \
            Enter the "code" - the user created using referral system.',
        request=SwaggerCreateRequestSerializer,
        responses={
            status.HTTP_201_CREATED: UserCreateSerializer,
            status.HTTP_400_BAD_REQUEST: DummyDetailSerializer,
            status.HTTP_404_NOT_FOUND: DummyDetailSerializer,
            status.HTTP_500_INTERNAL_SERVER_ERROR: DummyDetailSerializer,
        },
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class UserDeleteView(DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserDestroySerializer
    permission_classes = (IsAuthenticated, UserDeletePermission)

    @extend_schema(
        summary='Delete user. Need authorization!',
        responses={
            status.HTTP_204_NO_CONTENT: None,
            status.HTTP_400_BAD_REQUEST: DummyDetailSerializer,
            status.HTTP_401_UNAUTHORIZED: DummyDetailSerializer,
            status.HTTP_403_FORBIDDEN: DummyDetailSerializer,
            status.HTTP_404_NOT_FOUND: DummyDetailSerializer,
            status.HTTP_500_INTERNAL_SERVER_ERROR: DummyDetailSerializer,
        },
    )
    def delete(self, request, *args, **kwargs):
        try:
            obj = self.queryset.get(pk=kwargs.get('pk'))
            obj.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except User.DoesNotExist:
            return Response({"detail": "The requested object does not exist."}, status=status.HTTP_404_NOT_FOUND)

from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework import status
from rest_framework.generics import CreateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from ref_codes.models import RefCode
from ref_codes.permissions import RefCodeDeletePermission
from ref_codes.serializers import RefCodeCreateSerializer, RefCodeDestroySerializer, GetRefCodeByEmailSerializer, \
    SwaggerRequestSerializer, DummyDetailSerializer


class RefCodeCreateView(CreateAPIView):
    queryset = RefCode.objects.all()
    serializer_class = RefCodeCreateSerializer
    permission_classes = (IsAuthenticated,)

    @extend_schema(
        summary='Create referral number. Need authorization!',
        request=SwaggerRequestSerializer,
        responses={
            status.HTTP_201_CREATED: RefCodeCreateSerializer,
            status.HTTP_400_BAD_REQUEST: DummyDetailSerializer,
            status.HTTP_401_UNAUTHORIZED: DummyDetailSerializer,
            status.HTTP_404_NOT_FOUND: DummyDetailSerializer,
            status.HTTP_500_INTERNAL_SERVER_ERROR: DummyDetailSerializer,
        },
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class RefCodeDeleteView(DestroyAPIView):
    queryset = RefCode.objects.all()
    serializer_class = RefCodeDestroySerializer
    permission_classes = (IsAuthenticated, RefCodeDeletePermission)

    @extend_schema(
        summary='Delete referral number. Need authorization!',
        responses={
            status.HTTP_400_BAD_REQUEST: DummyDetailSerializer,
            status.HTTP_401_UNAUTHORIZED: DummyDetailSerializer,
            status.HTTP_404_NOT_FOUND: DummyDetailSerializer,
            status.HTTP_500_INTERNAL_SERVER_ERROR: DummyDetailSerializer,
        },
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


class GetRefCodeByEmail(APIView):
    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        if not email:
            return Response({'error': 'Email is required'}, status=status.HTTP_400_BAD_REQUEST)

        ref_code_obj = RefCode.objects.filter(user__email=email, is_active=True).first()
        if ref_code_obj:
            return Response(GetRefCodeByEmailSerializer(ref_code_obj).data, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'No active referral number found for the provided email'},
                            status=status.HTTP_404_NOT_FOUND)

from rest_framework import status
from rest_framework.generics import CreateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from ref_codes.models import RefCode
from ref_codes.serializers import RefCodeCreateSerializer, RefCodeDestroySerializer, GetRefCodeByEmailSerializer


class RefCodeCreateView(CreateAPIView):
    queryset = RefCode.objects.all()
    serializer_class = RefCodeCreateSerializer
    permission_classes = (IsAuthenticated,)


class RefCodeDeleteView(DestroyAPIView):
    queryset = RefCode.objects.all()
    serializer_class = RefCodeDestroySerializer
    permission_classes = (IsAuthenticated,)


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

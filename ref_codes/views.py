from rest_framework.generics import CreateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated

from ref_codes.models import RefCode
from ref_codes.serializers import RefCodeCreateSerializer, RefCodeDestroySerializer


class RefCodeCreateView(CreateAPIView):
    model = RefCode
    serializer_class = RefCodeCreateSerializer
    permission_classes = (IsAuthenticated,)


class RefCodeDeleteView(DestroyAPIView):
    queryset = RefCode.objects.all()
    serializer_class = RefCodeDestroySerializer
    permission_classes = (IsAuthenticated,)

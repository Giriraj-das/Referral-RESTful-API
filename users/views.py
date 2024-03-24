from django.db.models import Count
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated

from users.models import User
from users.serializers import UserListSerializer, UserCreateSerializer, UserDestroySerializer


class UserListView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer

    def get(self, request, *args, **kwargs):
        ref_id = request.GET.get('ref_id', None)
        if ref_id:
            self.queryset = self.queryset.filter(referer_user_id=ref_id)

        return super().get(request, *args, **kwargs)


class UserCreateView(CreateAPIView):
    model = User.objects.all()
    serializer_class = UserCreateSerializer


class UserDeleteView(DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserDestroySerializer
    permission_classes = (IsAuthenticated,)

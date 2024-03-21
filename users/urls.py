from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users import views

app_name = 'users'

urlpatterns = [
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    path('', views.UserListView.as_view(), name='users_list'),
    path('create/', views.UserCreateView.as_view(), name='create_user'),
]

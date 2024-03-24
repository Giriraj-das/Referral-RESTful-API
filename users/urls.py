from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users import views

urlpatterns = [
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    path('', views.UserListView.as_view()),
    path('create/<code>/', views.UserCreateView.as_view()),
    path('<int:pk>/delete/', views.UserDeleteView.as_view()),
]

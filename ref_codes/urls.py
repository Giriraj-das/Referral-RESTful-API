from django.urls import path

from ref_codes import views

urlpatterns = [
    path('create/', views.RefCodeCreateView.as_view()),
    path('<int:pk>/delete/', views.RefCodeDeleteView.as_view()),
]

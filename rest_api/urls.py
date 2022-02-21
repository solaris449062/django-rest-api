from django.urls import path

from rest_api import views

urlpatterns = [
    path('test-url/', views.TestAPIView.as_view()),
]


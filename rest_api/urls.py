from django.urls import path, include

from rest_framework.routers import DefaultRouter

from rest_api import views

router = DefaultRouter()
router.register('test-url-viewset', views.TestViewSet, base_name='test-url-viewset')

urlpatterns = [
    path('test-url/', views.TestAPIView.as_view()),
    path('', include(router.urls)),
]


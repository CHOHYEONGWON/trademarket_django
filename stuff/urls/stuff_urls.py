from django.urls import path, include
from rest_framework.routers import DefaultRouter
from stuff import views

router = DefaultRouter()
router.register('', views.StuffViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
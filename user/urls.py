from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'profiles', ProfileViewSet, basename='profile')
router.register(r'service-providers', ServiceProviderViewSet, basename='serviceprovider')


urlpatterns = router.urls

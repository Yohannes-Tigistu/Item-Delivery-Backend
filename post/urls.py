from rest_framework.routers import DefaultRouter
from rest_framework_nested.routers import NestedDefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'services', ServiceViewSet, basename='service')

nested_router = NestedDefaultRouter(router, r'services', lookup='service')
nested_router.register(r'paths', PathViewSet, basename='path')

urlpatterns = router.urls + nested_router.urls
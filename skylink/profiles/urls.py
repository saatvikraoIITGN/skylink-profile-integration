from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProfileViewSet, index

router = DefaultRouter()
router.register(r'profiles', ProfileViewSet)

urlpatterns = [
    path('', index, name='index'),
    path('api/', include(router.urls)),
]
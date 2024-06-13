from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductoviewSet

router = DefaultRouter()
router.register(r'productos', ProductoviewSet, basename='producto')

urlpatterns = [
    path('', include(router.urls)),
]

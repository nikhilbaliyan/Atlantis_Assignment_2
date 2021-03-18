from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('v1', views.UserViewSet)
router.register('find_user', views.CustomerModelViewSet)

urlpatterns = [
    path('api/', include(router.urls), name='users'),
]

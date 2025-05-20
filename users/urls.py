from django.urls import path
from .views import signin, signup, UserViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('user/', UserViewSet, basename = 'user')

urlpatterns = [
    path('signin/', signin, name = 'signin'),
    path('signup/', signup, name = 'signup')
] + router.urls
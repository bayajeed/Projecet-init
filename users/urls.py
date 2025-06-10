from django.urls import path
from .views import signin, signup, UserViewSet
from rest_framework.routers import DefaultRouter
from django.urls import include, re_path

router = DefaultRouter()
router.register(r'users', UserViewSet, basename = 'users')

urlpatterns = [
    # re_path(r'^', include(router.urls)), # ei line dile nicher (+ router.urls) eita na likleo hobe
    path('signin/', signin, name = 'signin'),
    path('signup/', signup, name = 'signup')
] + router.urls
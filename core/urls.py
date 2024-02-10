
from django.urls import path, include
from rest_framework import routers
from .views import UserCreate,hi
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
TokenVerifyView
)


router = routers.DefaultRouter()
router.register(r'user', UserCreate, basename="user")

urlpatterns = [
    path('', hi.as_view()),

    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('verify/', TokenVerifyView.as_view(), name='token_verify'),

       path('', include(router.urls)),

]

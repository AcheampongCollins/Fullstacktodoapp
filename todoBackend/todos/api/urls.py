from django.urls import path
from .views import  MyTokenObtainPairView
from . import views



from rest_framework_simplejwt.views import (
    TokenRefreshView,
)


urlpatterns = [
     path('', views.getRoute),
     path('token/',  MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
     path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
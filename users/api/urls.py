from django.urls import path
from .views import UserSignup, CustomAuthToken, LogoutView, TouristUserRegisterView

urlpatterns = [
    path('account/signup/', UserSignup.as_view(), name='signup'),
    path('account/login/', CustomAuthToken.as_view(), name='login'),
    path('account/logout/', LogoutView.as_view(), name='logout'),
    path('account/tourist/', TouristUserRegisterView.as_view(), name='tourist-register'),
]
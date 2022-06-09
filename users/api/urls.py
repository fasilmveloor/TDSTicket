from django.urls import path
from .views import UserSignup, CustomAuthToken, LogoutView

urlpatterns = [
    path('signup/', UserSignup.as_view(), name='signup'),
    path('login/', CustomAuthToken.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
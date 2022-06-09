from django.urls import path
from .views import TouristUserRegisterView

urlpatterns = [
    path('profile/', TouristUserRegisterView.as_view(), name='tourist-profile'),
]
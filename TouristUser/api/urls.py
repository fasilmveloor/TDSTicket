from django.urls import path
from .views import TouristUserRegisterView, TicketView, TeamMembersView

urlpatterns = [
    path('profile/', TouristUserRegisterView.as_view(), name='tourist-profile'),
    path('ticket/', TicketView.as_view(), name='tourist-ticket'),
    path('team-members/<int:pk>/', TeamMembersView.as_view(), name='tourist-team-members'),
]
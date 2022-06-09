from django.urls import path
from .views import TDUserView, TDUserViewset, TDTypeView, TDTypeViewset, AnnouncementsViewset, AnnouncementDetailView, TDUserUpdateView

urlpatterns = [
    path('tds/', TDUserViewset.as_view(), name='tds'),
    path('tds/<int:pk>/', TDUserView.as_view(), name='tds'),
    path('tdtype/', TDTypeViewset.as_view(), name='tdtype'),
    path('tdtype/<int:pk>/', TDTypeView.as_view(), name='tdtype'),
    path('announcements/', AnnouncementsViewset.as_view(), name='announcements'),
    path('announcements/<int:pk>/', AnnouncementDetailView.as_view(), name='announcements'),
    path('tds/update/', TDUserUpdateView.as_view(), name='tds-update'),
]
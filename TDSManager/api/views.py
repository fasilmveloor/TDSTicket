import rest_framework.response as response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView, ListAPIView, ListCreateAPIView, RetrieveUpdateAPIView
from TDSManager.models import TDSUser, TDType, Announcements
from .serializers import TDSUserSerializer, TDTypeSerializer, AnnouncementsSerializer
from users.api.permissions import IS_TDS
class TDTypeViewset(ListAPIView):
    queryset = TDType.objects.all()
    serializer_class = TDTypeSerializer

class TDTypeView(RetrieveAPIView):
    queryset = TDType.objects.all()
    serializer_class = TDTypeSerializer   

class TDUserViewset(ListCreateAPIView):
    queryset = TDSUser.objects.all()
    serializer_class = TDSUserSerializer
    permission_classes = [IsAuthenticated]

class TDUserView(RetrieveAPIView):
    queryset = TDSUser.objects.all()
    serializer_class = TDSUserSerializer
    permission_classes = [IsAuthenticated]

class AnnouncementsViewset(ListCreateAPIView):
    queryset = Announcements.objects.all()
    serializer_class = AnnouncementsSerializer
    permission_classes = [IsAuthenticated]

    def list(self, request):
        queryset = Announcements.objects.all().filter(tds=TDSUser.objects.get(user=request.user))
        serializer = AnnouncementsSerializer(queryset, many=True)
        return response.Response(serializer.data)

class AnnouncementDetailView(RetrieveAPIView):
    queryset = Announcements.objects.all()
    serializer_class = AnnouncementsSerializer
    permission_classes = [IsAuthenticated]
    
class TDUserUpdateView(RetrieveUpdateAPIView):
    queryset = TDSUser.objects.all()
    serializer_class = TDSUserSerializer
    permission_classes = [IsAuthenticated, IS_TDS]
    lookup_field = 'user'
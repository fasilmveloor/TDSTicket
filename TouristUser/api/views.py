from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from users.api.permissions import IsTourist
from TouristUser.models import TouristUser, Ticket, TeamMember
from .serializers import TeamMemberSerializer, TouristUserSerializer, TicketSerializer, TicketCreateSerializer

class TouristUserRegisterView(generics.GenericAPIView):
    queryset = TouristUser.objects.all()
    serializer_class = TouristUserSerializer
    permission_classes = (IsAuthenticated, IsTourist)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            "message": "Tourist profile Created successfully."
        })


class TicketView(generics.ListCreateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    #permission_classes = (IsAuthenticated)

    def list(self, request, *args, **kwargs):
        tourist = TouristUser.objects.get(user = self.request.user)
        tickets = Ticket.objects.filter(tourist = tourist)
        serializer = self.get_serializer(tickets, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = TicketCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            "message": "Ticket Created successfully."
        })

class TeamMembersView(generics.RetrieveAPIView):
    queryset = TeamMember.objects.all()
    serializer_class = TeamMemberSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        ticket = Ticket.objects.get(pk = self.kwargs['pk'])
        team_members = ticket.team_members.all()
        serializer = self.get_serializer(team_members, many=True)
        return Response(serializer.data)
    
class TeamMemberViewset(generics.ListCreateAPIView):
    queryset = TeamMember.objects.all()
    serializer_class = TeamMemberSerializer
    #permission_classes = [IsAuthenticated]

    

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        s = serializer.save()
        serializer = self.get_serializer(s)
        return Response({
            "message": "Team member added successfully.",
            "team_member": serializer.data['id']
        })

class TouristProfileView(generics.RetrieveUpdateAPIView):
    queryset = TouristUser.objects.all()
    serializer_class = TouristUserSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        tourist = TouristUser.objects.get(user = self.request.user)
        serializer = self.get_serializer(tourist)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        tourist = TouristUser.objects.get(user = self.request.user)
        serializer = self.get_serializer(tourist, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            "message": "Tourist profile updated successfully."
        })
from .serializers import TouristUserSerializer
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from users.api.permissions import IsTourist
from TouristUser.models import TouristUser

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
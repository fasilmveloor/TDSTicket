from tokenize import group
from rest_framework import serializers
from TouristUser.models import TouristUser, Ticket, TeamMember
from TouristUser import utilities
from TDSManager.models import TDSUser
from TouristUser.facemask.detect_mask_video import checkImage

class TouristUserSerializer(serializers.ModelSerializer):
    vaccination_certificate = serializers.FileField(write_only=True)

    def save(self, **kwargs):
        user = self.context['request'].user
        first_name=self.validated_data['first_name']
        last_name=self.validated_data['last_name']
        date_of_birth=self.validated_data['date_of_birth']
        vaccination_certificate=self.validated_data['vaccination_certificate']
        is_vaccinated = utilities.getVaccinationStatus(vaccination_certificate)
        profile_image=self.validated_data['profile_image']
        address=self.validated_data['address']
        phone_number=self.validated_data['phone_number']
        touristUser = TouristUser(first_name=first_name, last_name=last_name, 
                    date_of_birth=date_of_birth,is_vaccinated=is_vaccinated,
                    profile_image=profile_image, address=address,
                    phone_number=phone_number, user=user)
        touristUser.save()
        return touristUser
        
    class Meta:
        model = TouristUser
        fields = ('first_name', 'last_name', 'date_of_birth', 'profile_image', 'vaccination_certificate',  'phone_number', 'address')
        extra_kwargs = {
            'vaccination_certificate': {'write_only': True}
        }

class TeamMemberSerializer(serializers.ModelSerializer):
    #ticket = serializers.PrimaryKeyRelatedField(queryset=Ticket.objects.all(), write_only=True)

    def save(self, **kwargs):
        name=self.validated_data['name']
        dob=self.validated_data['dob']
        vaccination_status=self.validated_data['vaccination_status']
        vaccination_certificate = self.validated_data['vaccination_certificate']
        teamMember = TeamMember(name=name, dob=dob, vaccination_status=vaccination_status, vaccination_certificate=vaccination_certificate)
        teamMember.save()
        return teamMember

    class Meta:
        model = TeamMember
        fields = ('id', 'name', 'dob', 'vaccination_status', 'vaccination_certificate')

class TicketSerializer(serializers.ModelSerializer):
    team_members = TeamMemberSerializer(many=True)

    def save(self, **kwargs):
        tourist = TouristUser.objects.get(user = self.validated_data['request'].user)
        tds = TDSUser.objects.get(pk = self.validated_data['tds'])
        no_of_Tickets = self.validated_data['no_of_Tickets']
        no_of_adults = self.validated_data['no_of_adults']
        no_of_children = self.validated_data['no_of_children']
        total_price = tds.price * no_of_Tickets 
        visiting_date = self.validated_data['visiting_date']
        group_image = self.validated_data['group_image']
        message = checkImage(group_image)
        if message != "All faces are masked" :
            raise serializers.ValidationError(message)
        team_members = self.validated_data['team_members']
        teamMember = TeamMemberSerializer(data=team_members, many=True)
        teamMember.is_valid()
        teamMember.save()
        ticket = Ticket(tourist=tourist, tds=tds, no_of_Tickets=no_of_Tickets, no_of_adults=no_of_adults, no_of_children=no_of_children, total_price=total_price, visiting_date=visiting_date, group_image=group_image, team_members=teamMember.data)
        ticket.save()
        return ticket

        

    class Meta:
        model = Ticket
        fields = "__all__"
    
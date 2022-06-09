from rest_framework import serializers
from TouristUser.models import TouristUser
from TouristUser import utilities

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
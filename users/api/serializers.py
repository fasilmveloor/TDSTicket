from asyncore import write
from rest_framework import serializers
from users.models import User, TouristUser
from users import utilities

class UserSignupSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    role = serializers.CharField(write_only=True)

    def save(self, **kwargs):
        user = User(
            username=self.validated_data['username'],
            email=self.validated_data['email'],
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'password': 'Passwords must match.'})
        user.set_password(password)
        if self.validated_data['role'] == 'tourist':
            user.is_tourist = True
        elif self.validated_data['role'] == 'tds':
            user.is_tds = True
        else:
            raise serializers.ValidationError({'role': 'Role must be either tourist or tds.'})
        user.save()
        return user

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password2', 'role')
        extra_kwargs = {
            'password': {'write_only': True},
            'role': {'write_only': True}
        }


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
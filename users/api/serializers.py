from rest_framework import serializers
from users.models import User
from TDSManager.models import TDType
from TouristUser import utilities

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
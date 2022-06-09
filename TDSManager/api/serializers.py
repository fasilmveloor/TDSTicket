from rest_framework import serializers
from TDSManager.models import TDSUser, TDType, Announcements

class TDSUserSerializer(serializers.ModelSerializer):

    def save(self, **kwargs):
        user = self.context['request'].user
        name=self.validated_data['name']
        opening_time=self.validated_data['opening_time']
        closing_time = self.validated_data['closing_time']
        holydays = self.validated_data['holydays']
        address = self.validated_data['address']
        phone_number = self.validated_data['phone_number']
        ticket_fair = self.validated_data['ticket_fair']
        visitor_min_age = self.validated_data['visitor_min_age']
        description = self.validated_data['description']
        type = TDType.objects.get(type=self.validated_data['type'])
        tdsUser = TDSUser(name=name, opening_time=opening_time, closing_time=closing_time,
                    holydays=holydays, address=address, phone_number=phone_number,
                    ticket_fair=ticket_fair, visitor_min_age=visitor_min_age,
                    description=description, type=type, user=user)
        tdsUser.save()
        return tdsUser

    class Meta:
        model = TDSUser
        fields = ('tdid','name', 'opening_time', 'closing_time', 'holydays', 'address', 'ticket_fair', 'phone_number', 'visitor_min_age', 'description', 'type')


class TDTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TDType
        fields = ('id','type','description')

class AnnouncementsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announcements
        fields = ('id','title','description','date','tds')
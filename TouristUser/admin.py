from django.contrib import admin
from .models import TouristUser, Ticket, TeamMember
# Register your models here.

class TouristUserAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'last_name', 'date_of_birth', 'is_vaccinated', 'address', 'phone_number')

    class Meta:
        model = TouristUser

class TicketAdmin(admin.ModelAdmin):
    list_display = ('ticketid', 'tourist', 'tds', 'no_of_Tickets', 'no_of_adults', 'no_of_children', 'total_price', 'booked_date', 'visiting_date')

    class Meta:
        model = Ticket

class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'dob', 'vaccination_status')

    class Meta:
        model = TeamMember

admin.site.register(TouristUser, TouristUserAdmin)
admin.site.register(Ticket, TicketAdmin)
admin.site.register(TeamMember, TeamMemberAdmin)
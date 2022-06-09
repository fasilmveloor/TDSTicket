from django.contrib import admin
from .models import TDSUser, TDType, Announcements
# Register your models here.

class TDSUserAdmin(admin.ModelAdmin):
    list_display = ('user', 'type', 'opening_time', 'closing_time', 'holydays', 'address', 'ticket_fair', 'phone_number', 'visitor_min_age', 'description')
    list_filter = ('type',)

    class Meta:
        model = TDSUser

class TDTypeAdmin(admin.ModelAdmin):
    list_display = ('id','type', 'description')

    class Meta:
        model = TDType

class AnnouncementsAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'date', 'tds')

    class Meta:
        model = Announcements

admin.site.register(TDSUser, TDSUserAdmin)
admin.site.register(TDType, TDTypeAdmin)
admin.site.register(Announcements, AnnouncementsAdmin)
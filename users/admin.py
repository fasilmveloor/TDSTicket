from dataclasses import field
from django.contrib import admin
from .models import TouristUser, TDSUser, User, TDType
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'is_tourist', 'is_tds')



class TouristUserAdmin(admin.ModelAdmin):
    class Meta:
        model = TouristUser
        fields = ('first_name', 'last_name', 'date_of_birth', 'profile_image', 'phone_number', 'address')

class TDTypeAdmin(admin.ModelAdmin):
    class Meta:
        model = TDType
        fields = ('name', 'description')

admin.site.register(User, UserAdmin)
admin.site.register(TouristUser, TouristUserAdmin)
admin.site.register(TDSUser)
admin.site.register(TDType, TDTypeAdmin)
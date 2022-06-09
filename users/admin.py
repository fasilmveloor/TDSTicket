from dataclasses import field
from django.contrib import admin
from .models import User
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'password', 'is_tourist', 'is_tds')
    list_filter = ('is_tourist', 'is_tds')

    class Meta:
        model = User
        



admin.site.register(User, UserAdmin)

from django.contrib import admin
from .models import User, Video
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

class CustomUserAdmin(UserAdmin):
    # Add your customizations here
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'date_joined')

admin.site.unregister(User)
admin.site.register(Video)
admin.site.register(User, CustomUserAdmin)
from django.contrib import admin
from main.models import *
from django.contrib.auth.admin import UserAdmin
from main.forms import *

class UserProfileInline(admin.StackedInline):
    model = UserProfile

admin.site.register(UserProfile)

class MyUserAdmin(UserAdmin):
  # form = CustomUserChangeForm
  # add_form = CustomUserCreationForm
  inlines = [UserProfileInline]
  list_display = ['id', 'email', 'first_name', 'last_name', 'date_joined']

admin.site.unregister(User)
admin.site.register(User, MyUserAdmin)

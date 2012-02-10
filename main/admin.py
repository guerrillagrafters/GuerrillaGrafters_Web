
from django.contrib import admin
from main.models import *
from django.contrib.auth.admin import UserAdmin
from main.forms import *
from main.decorators import *
from main.unicodecsv import *

class UserProfileInline(admin.StackedInline):
    model = UserProfile

admin.site.register(UserProfile)

@allowEmptyQuerySetForActions(['export_users'])
class MyUserAdmin(UserAdmin):
  # form = CustomUserChangeForm
  # add_form = CustomUserCreationForm
  actions = ['export_users']
  inlines = [UserProfileInline]
  list_display = ['id', 'email', 'first_name', 'last_name', 'date_joined']

  def export_users(self, request, queryset):
    response = HttpResponse(mimetype='text/csv')
    response['Content-Disposition'] = 'attachment; filename=guerrillagrafters_users.csv'
    writer = UnicodeWriter(response)

    for user in User.objects.all():
      writer.writerow([user.email, user.first_name, user.last_name, str(user.date_joined)])

    return response


admin.site.unregister(User)
admin.site.register(User, MyUserAdmin)

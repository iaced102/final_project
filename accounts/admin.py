from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from .forms import ManageUserForm

# Register your models here.

class CustomerUserAdmin(UserAdmin):
    model = User
    list_display = ['username', 'email', 'first_name', 'last_name', 'is_staff']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('phone_number',)}),
        (None, {'fields': ('is_teacher',)}), 
    )
    add_fieldsets = (
        (None, {'fields': ('phone_number',)}), 
        (None, {'fields': ('is_teacher',)}), 
        (None, {'fields': ('email',)})
    ) + UserAdmin.add_fieldsets 


admin.site.register(User, CustomerUserAdmin)
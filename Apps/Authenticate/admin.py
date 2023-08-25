from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import Error

User = get_user_model()

# Register your models here.
class UserAccountAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'is_active', 'is_staff', 'first_login')
    list_display_links = ('email', 'first_name', 'last_name')
    search_fields = ('email', 'first_name', 'last_name')
    list_per_page = 25

admin.site.register(User, UserAccountAdmin) 
admin.site.register(Error)

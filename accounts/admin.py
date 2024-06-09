from django.contrib import admin

from accounts.models import SchoolMember, User
# Register your models here.

@admin.register(SchoolMember)
class SchoolMember(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'member_id',  'occupation', 'email', 'created', 'updated')
    list_filter = ('occupation', 'created', 'updated')
    search_fields = ('first_name', 'occupation', 'last_name', 'member_id', 'email')
    ordering = ('created',)

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'member', 'is_staff', 'is_active',)
    search_fields = ('username', 'email', 'member__first_name', 'member__last_name')
    list_filter = ('is_staff', 'is_active', 'groups')


admin.site.register(User, CustomUserAdmin)
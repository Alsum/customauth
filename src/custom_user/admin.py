from django.contrib import admin

from models import CustomUser


class CustomUserAdmin(admin.ModelAdmin):
    search_fields = ['username', 'email']
    fields = ('email', 'username', 'first_name', 'last_name'
              , 'is_staff', 'is_active', 'is_superuser', 'password',
              'groups','user_permissions','last_login', 'date_joined')
    filter_horizontal = ('groups','user_permissions')
    list_display = ['email', 'first_name', 'last_name', 'is_staff']
    list_filter = ['is_staff', 'is_active', 'is_superuser']
    readonly_fields = ['password', 'date_joined']

    class Meta:
        model = CustomUser


admin.site.register(CustomUser, CustomUserAdmin)

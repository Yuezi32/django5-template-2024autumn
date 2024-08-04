from django.contrib import admin

# Register your models here.

from .models import User

# 用于控制在Django管理后台的表显示哪些
class UserDjangoAdmin(admin.ModelAdmin):
    list_display = (
        "uid",
        "account",
        "nickname",
        "group",
        "status",
        "create_datetime",
        "password",
        "access_token",
        "access_token_expire",
        "last_login_datetime",
    )
    
admin.site.register(User, UserDjangoAdmin)
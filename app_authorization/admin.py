from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin

from app_authorization.models import Profile


admin.site.register(Profile)

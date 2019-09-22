from django.contrib import admin
from django.contrib.auth.models import Group

from authapp.models import WebUser

admin.site.register(WebUser)
admin.site.unregister(Group)

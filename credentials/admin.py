from django.contrib import admin
from .models import Credentials, CredentialsAdmin, Bug, BugAdmin


admin.site.register(Credentials, CredentialsAdmin)
admin.site.register(Bug,BugAdmin)
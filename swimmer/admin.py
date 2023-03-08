from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from import_export.admin import ImportExportModelAdmin
from .models import Swimling
from .resources import SwimlingResource


class SwimlingAdmin(ImportExportModelAdmin):
    resource_class = SwimlingResource


admin.site.register(Swimling, SwimlingAdmin)

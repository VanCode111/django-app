from django.contrib import admin
from .models import Cleaning
from import_export.admin import ImportExportActionModelAdmin

class RecordsExcel(ImportExportActionModelAdmin):
    pass


admin.site.register(Cleaning, RecordsExcel)
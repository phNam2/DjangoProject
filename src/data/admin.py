from django.contrib import admin

# Register your models here.
from .models import Manhattan
from import_export.admin import ImportExportModelAdmin

# admin.site.register(Manhattan)
@admin.register(Manhattan)
class ViewAdmin(ImportExportModelAdmin):
	pass
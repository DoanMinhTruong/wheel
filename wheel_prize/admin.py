# from tkinter import EventType
from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
# Register your models here.
admin.site.register(Event )
admin.site.register(EventPrize)
admin.site.register(PrizeWinPercent)
# admin.site.register(PrizeLog)
@admin.register(PrizeLog)
class PrizeLogAdmin(ImportExportModelAdmin):
    pass
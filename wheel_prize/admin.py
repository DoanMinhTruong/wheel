from tkinter import EventType
from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Event )
admin.site.register(EventPrize)
admin.site.register(PrizeWinPercent)
admin.site.register(PrizeLog)
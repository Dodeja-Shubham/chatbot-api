from django.contrib import admin
import requests
from .models import Send_Message, Schedule_Message, Conversation
# Register your models here.

class Send_Message_Admin(admin.ModelAdmin):
    list_display = ('id', 'channel', 'text')

class Schedule_Message_Admin(admin.ModelAdmin):
    list_display = ('id', 'channel', 'text')

admin.site.register(Send_Message, Send_Message_Admin)
admin.site.register(Schedule_Message, Schedule_Message_Admin)
admin.site.register(Conversation)
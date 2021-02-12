from django.contrib import admin
from .models import *





@admin.register(ContactMe)
class ContactMeAdmin(admin.ModelAdmin):
	list_display = ['name', 'email', 'message',]

from django.contrib import admin

# Register your models here.

from .models import *



@admin.register(ContactMe)
class ContactMeAdmin(admin.ModelAdmin):
	list_display = ['name', 'email', 'message',]

from django.contrib import admin
from .models import *
# Register your models here.



class PhonebookAdmin(admin.ModelAdmin):
    list_display = ('name','phone')

admin.site.register(Phonebook,PhonebookAdmin)
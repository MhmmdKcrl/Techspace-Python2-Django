from django.contrib import admin

# Register your models here.

from .models import Contact, Subscribers

admin.site.register(Contact)
admin.site.register(Subscribers)
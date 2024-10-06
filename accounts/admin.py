from django.contrib import admin

# Register your models here.


from accounts.models import BlackListedIPAddresses


admin.site.register(BlackListedIPAddresses)
from django.db import models
# from django.contrib.auth.models import AbstractUser


# class User(AbstractUser):
#     photo = models.ImageField('photo', upload_to='user_profiles/', null=True, blank=True)
#     bio = models.CharField('bio', max_length=255, null=True, blank=True)



class BlackListedIPAddresses(models.Model):
    ip_address = models.GenericIPAddressField()

    def __str__(self):
        return self.ip_address

from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.utils.text import slugify

from recipes.models import Recipe


@receiver(pre_save, sender=Recipe)
def my_callback(instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.title)


@receiver(post_save, sender=Recipe)
def make_slug(sender, instance, created, **kwargs):
    if created:
        instance.slug = slugify(instance.title)
        instance.save()
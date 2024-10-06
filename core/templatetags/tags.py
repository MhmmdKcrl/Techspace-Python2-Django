from django import template
# import warnings
# from django.utils.deprecation import RemovedInDjango51Warning

register = template.Library()

from  recipes.models import Category, Tags


@register.simple_tag
def get_categories(limit=5):
    categories = Category.objects.all()[:limit]
    # print(categories, "--------------")
    return categories


@register.simple_tag
def get_tags():
    tags = Tags.objects.all()
    return tags




@register.filter
def capitalize(value):
    return value.capitalize()


@register.filter
def upper(value):
    return value.upper()


@register.filter
def lower(value):
    return value.lower()

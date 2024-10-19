from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.utils.http import url_has_allowed_host_and_scheme

from celery import shared_task
from food import settings
from core.models import Subscribers
from recipes.models import Recipe
import time
from datetime import datetime, timedelta


import time
from celery import shared_task


@shared_task
def my_task():
    print('Start...')
    time.sleep(10)
    print('End...')



@shared_task
def mail_to_subscribers():
    subs = list(Subscribers.objects.values_list('email', flat=True))
    recipes = Recipe.objects.all()[:2]

    subject = "New Recipes"
    text_content = "This is a notification about new recipes."
    for sub in subs:
        message = render_to_string('email-subscribers.html',
                                   {'recipes': recipes, 
                                    'mail': sub}
                                    )
        msg = EmailMultiAlternatives(subject, text_content, settings.EMAIL_HOST_USER, [sub])
        msg.attach_alternative(message, "text/html")
        msg.send()
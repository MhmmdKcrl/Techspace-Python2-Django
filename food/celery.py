# django_celery/celery.py

import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "food.settings")
app = Celery("django_celery")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()



# python3 -m celery -A food worker -l info

# celery -A food worker --beat --scheduler django --loglevel=info 



# py -m celery -A food worker -l info --pool=threads 

# celery -A food beat --loglevel=info --scheduler django_celery_beat.schedulers:DatabaseScheduler
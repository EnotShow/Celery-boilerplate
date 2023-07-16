import os

from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

app = Celery('project')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Add Celery Beat schedule
app.conf.beat_schedule = {
    'create_random_model': {
        'task': 'app.tasks.create_random_model',
        'schedule': 60.0,  # Set the schedule in seconds (e.g., every 60 seconds)
    },
}

# Load task modules from all registered Django apps.
app.autodiscover_tasks()

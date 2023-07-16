import string
import random

from celery import shared_task

from app.models import TestModel


@shared_task
def create_random_model():
    characters = string.ascii_letters + string.digits + string.punctuation
    title = ''.join(random.choice(characters) for _ in range(21))
    test_model = TestModel(title=title)
    test_model.save()
    return f'{title} model created!'

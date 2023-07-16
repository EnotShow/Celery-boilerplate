from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from django.urls import path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from django.conf import settings

from app.views import TestModelView

urlpatterns = [
    path('model/', TestModelView.as_view(), name='model'),
]

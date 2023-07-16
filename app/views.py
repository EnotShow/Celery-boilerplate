from django.shortcuts import render
from django.views import generic

from app.models import TestModel


class TestModelView(generic.ListView):
    model = TestModel
    queryset = TestModel.objects.all()

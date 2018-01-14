# -*- coding: utf-8
from django.apps import AppConfig
import os


class ExampleAppConfig(AppConfig):
    name = 'example'
    path = os.path.abspath(os.path.dirname(__file__))

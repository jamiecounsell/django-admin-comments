# -*- coding: utf-8 -*-
from __future__ import print_function

from django.contrib.auth.models import User
from django.test import Client, TestCase


class AdminTestCase(TestCase):

    def setUp(self):
        self.password = 'secret'
        self.admin= User.objects.create_superuser(
            'admin', 'example-email@website.com', self.password)
        self.client = Client()

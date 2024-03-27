# -*- coding: utf-8 -*-
from __future__ import print_function

from django.test import TestCase
from admin_comments.helpers import get_class_from_str


class HelpersTestCase(TestCase):
    def test_get_class_from_str_imports_global(self):
        from math import pi as TargetKlass

        ResultKlass = get_class_from_str("math.pi")
        self.assertEqual(TargetKlass, ResultKlass)

    def test_get_class_from_str_imports_builtin(self):
        from django.core.wsgi import WSGIHandler as TargetKlass

        ResultKlass = get_class_from_str("django.core.wsgi.WSGIHandler")
        self.assertEqual(TargetKlass, ResultKlass)

    def test_get_class_from_str_imports_custom(self):
        from tests.forms import MyTestForm as TargetKlass

        ResultKlass = get_class_from_str("tests.forms.MyTestForm")
        self.assertEqual(TargetKlass, ResultKlass)

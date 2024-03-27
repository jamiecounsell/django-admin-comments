# -*- coding: utf-8 -*-
from __future__ import print_function

from django.test import TransactionTestCase
from admin_comments.forms import CommentInlineForm
from example.example.models import Musician
from django.core.management import call_command

try:
    from django.urls import reverse
except ImportError:
    from django.core.urlresolvers import reverse


class AdminTestCase(TransactionTestCase):
    def test_inline_comment_is_readonly_for_existing(self):
        instance = Musician(first_name="Test", last_name="Test", instrument="Test")
        instance.id = 1
        inlineform = CommentInlineForm(instance=instance)
        attrs = inlineform.fields["comment"].widget.attrs
        readonly = attrs["readonly"] if hasattr(attrs, "readonly") else False
        self.assertEqual(attrs["readonly"], True)

    def test_inline_comment_isnt_readonly_for_new(self):
        inlineform = CommentInlineForm(instance=None)
        attrs = inlineform.fields["comment"].widget.attrs
        readonly = attrs["readonly"] if hasattr(attrs, "readonly") else False
        self.assertEqual(readonly, False)

    def test_inline_comment_has_no_border_for_existing(self):
        inlineform = CommentInlineForm(instance=Musician())
        attrs = inlineform.fields["comment"].widget.attrs
        border = attrs["border"] if hasattr(attrs, "border") else False
        self.assertEqual(border, 0)

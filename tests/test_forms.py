# -*- coding: utf-8 -*-
from __future__ import print_function

from django.test import TestCase, override_settings
from admin_comments.forms import CommentInlineForm, CommentInlineFormset
from example.example.models import Musician

try:
    from django.urls import reverse
except ImportError:
    from django.core.urlresolvers import reverse


class AdminTestCase(TestCase):

    def test_inline_comment_is_readonly_for_existing(self):
        inlineform = CommentInlineForm(instance = Musician)
        attrs = inlineform.fields['comment'].widget.attrs
        self.assertEqual(attrs['readonly'], True)

    def test_inline_comment_has_no_border_for_existing(self):
        inlineform = CommentInlineForm(instance = Musician)
        attrs = inlineform.fields['comment'].widget.attrs
        self.assertEqual(attrs['border'], 0)

    def test_inline_comment_isnt_readonly_for_new(self):
        inlineform = CommentInlineForm(instance = None)
        attrs = inlineform.fields['comment'].widget.attrs
        readonly = attrs['readonly'] if hasattr(attrs, 'readonly') else False
        self.assertEqual(readonly, False)

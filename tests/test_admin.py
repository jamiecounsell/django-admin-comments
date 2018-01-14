# -*- coding: utf-8 -*-
from __future__ import print_function

from django.contrib.auth.models import User
from django.test import Client, TestCase, override_settings
from django.conf.urls import url
from django.contrib.admin import site
from admin_comments.models import Comment
from admin_comments.admin import CommentInline
from example.example.models import Musician

from example.example import urls

try:
    from django.urls import reverse
except ImportError:
    from django.core.urlresolvers import reverse


class AdminTestCase(TestCase):

    def setUp(self):
        super(AdminTestCase, self).setUp()
        self.password = 'secret'
        self.admin = User.objects.create_superuser(
            'admin', 'example-email@website.com', self.password)
        self.client = Client()
        self.urls = urls.urlpatterns

    @override_settings(ADMIN_COMMENTS_FORM_CLASS = 'tests.forms.MyTestForm')
    def test_inline_honors_form_class_setting(self):
        from tests.forms import MyTestForm as Target
        inline = CommentInline(Comment, site)
        self.assertEqual(inline.form, Target)

    @override_settings(ADMIN_COMMENTS_FORMSET_CLASS = 'tests.forms.MyTestFormset')
    def test_inline_honors_formset_class_setting(self):
        from tests.forms import MyTestFormset as Target
        inline = CommentInline(Comment, site)
        self.assertEqual(inline.formset, Target)

    @override_settings(ADMIN_COMMENTS_SHOW_EMPTY = True)
    def test_inline_honors_show_empty_true_setting(self):
        inline = CommentInline(Comment, site)
        self.assertEqual(inline.extra, 1)

    @override_settings(ADMIN_COMMENTS_SHOW_EMPTY = False)
    def test_inline_honors_show_empty_false_setting(self):
        inline = CommentInline(Comment, site)
        self.assertEqual(inline.extra, 0)

    @override_settings(ADMIN_COMMENTS_SHOW_EMPTY = None)
    def test_inline_honors_show_empty_unset_setting(self):
        from django.conf import settings
        del settings.ADMIN_COMMENTS_SHOW_EMPTY
        inline = CommentInline(Comment, site)
        self.assertEqual(inline.extra, 0)

    def test_site_register_succeeds(self):
        from django.contrib.admin import AdminSite, ModelAdmin

        site = AdminSite()

        class MusicianAdmin(ModelAdmin):
            inlines = [CommentInline]

        site.register(Musician, MusicianAdmin)

    def test_admin_returns_form(self):
        from django.contrib.admin import AdminSite, ModelAdmin

        site = AdminSite()

        class MusicianAdmin(ModelAdmin):
            inlines = [CommentInline]

        site.register(Musician, MusicianAdmin)

        self.urls += url(r'^test/', site.urls),

        self.client.force_login(self.admin)
        resp = self.client.get(reverse("admin:example_musician_add"))

        self.assertContains(resp, "<td class=\"field-comment\">")

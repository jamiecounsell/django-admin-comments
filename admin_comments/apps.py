# -*- coding: utf-8
from django.apps import AppConfig


class DjangoAdminCommentsConfig(AppConfig):
    name = 'admin_comments'
    verbose_name = 'Comment'
    verbose_name_plural = verbose_name


__all__= ['DjangoAdminCommentsConfig']

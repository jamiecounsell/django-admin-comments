# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

User = get_user_model()


class Comment(models.Model):

    # Support integer and UUID primary keys
    object_id = models.CharField(
        max_length = 32
    )

    content_object = GenericForeignKey(
        "content_type",
        "object_id"
    )

    content_type = models.ForeignKey(
        ContentType,
        on_delete = models.CASCADE
    )

    user = models.ForeignKey(
        User,
        on_delete = models.SET_NULL,
        blank = False,
        null = True
    )

    time = models.DateTimeField(
        auto_now_add=True
    )

    comment = models.TextField(
        blank = False
    )

    def __str__(self):
        return self.time.strftime("%b. %d, %Y, %-I:%M %p")

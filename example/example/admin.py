from django.contrib import admin
from .models import Musician, Album
from admin_comments.admin import CommentInline


class MusicianAdmin(admin.ModelAdmin):
    inlines = [CommentInline]


class AlbumAdmin(admin.ModelAdmin):
    inlines = [CommentInline]


admin.site.register(Musician, MusicianAdmin)
admin.site.register(Album, AlbumAdmin)

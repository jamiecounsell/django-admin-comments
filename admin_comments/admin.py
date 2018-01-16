from django.contrib.contenttypes.admin import GenericTabularInline
from admin_comments.models import Comment
from admin_comments.helpers import get_class_from_str
from django.conf import settings


class CommentInline(GenericTabularInline):

    model = Comment

    readonly_fields = ('user',)

    classes = ['collapse']

    def __init__(self, *args, **kwargs):
        form_klass = getattr(
            settings,
            'ADMIN_COMMENTS_FORM_CLASS',
            'admin_comments.forms.CommentInlineForm')

        formset_klass = getattr(
            settings,
            'ADMIN_COMMENTS_FORMSET_CLASS',
            'admin_comments.forms.CommentInlineFormset')

        SHOW_EMPTY = getattr(settings, 'ADMIN_COMMENTS_SHOW_EMPTY', False)

        CommentForm = get_class_from_str(form_klass)
        CommentFormSet = get_class_from_str(formset_klass)

        self.form = CommentForm
        self.formset = CommentFormSet
        self.extra = 1 if SHOW_EMPTY else 0
        super(CommentInline, self).__init__(*args, **kwargs)

    def get_queryset(self, request):
        return super(CommentInline, self).get_queryset(request).order_by('-time')

    def has_delete_permission(self, request, obj=None):
        return False

    def get_formset(self, request, obj=None, **kwargs):
        formset = super(CommentInline, self).get_formset(
            request, obj, **kwargs)
        formset.current_user = request.user
        return formset


__all__ = ['CommentInline']

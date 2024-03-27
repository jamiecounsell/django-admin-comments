from django.contrib.contenttypes.admin import GenericTabularInline
from admin_comments.models import Comment, Attachment
from admin_comments.helpers import get_class_from_str
from django.conf import settings


class BaseInline:
    readonly_fields = ("user",)
    classes = []

    def __init__(self, *args, **kwargs):
        form_klass = getattr(
            settings,
            f"ADMIN_{self.kind.upper()}_FORM_CLASS",
            f"admin_comments.forms.{self.kind.capitalize()}InlineForm",
        )

        formset_klass = getattr(
            settings,
            f"ADMIN_{self.kind.upper()}_FORMSET_CLASS",
            f"admin_comments.forms.{self.kind.capitalize()}InlineFormset",
        )

        SHOW_EMPTY = getattr(settings, "ADMIN_COMMENTS_SHOW_EMPTY", False)

        self.form = get_class_from_str(form_klass)
        self.formset = get_class_from_str(formset_klass)
        self.extra = 1 if SHOW_EMPTY else 0
        super().__init__(*args, **kwargs)

    def get_queryset(self, request):
        return super().get_queryset(request).order_by("-time")

    def has_delete_permission(self, request, obj=None):
        return False

    def get_formset(self, request, obj=None, **kwargs):
        formset = super().get_formset(request, obj, **kwargs)
        formset.current_user = request.user
        return formset


class CommentInline(BaseInline, GenericTabularInline):
    kind = "Comment"
    model = Comment


class AttachmentInline(BaseInline, GenericTabularInline):
    kind = "Attachment"
    model = Attachment


__all__ = ["CommentInline", "AttachmentInline"]

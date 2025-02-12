from django.contrib import admin
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _

from unfold.admin import ModelAdmin as UnfoldModelAdmin
from unfold.decorators import display

from ..models import StudentProject


@admin.register(StudentProject)
class StudentProjectAdmin(UnfoldModelAdmin):
    list_display = ('name', 'display_photo')
    search_fields = ('name',)
    list_filter = ('specialty',)
    readonly_fields = ('display_photo',)

    @display(description=_("Фото"))
    def display_photo(self, obj):
        if obj.photo:
            return mark_safe(
                f'<img src="{obj.photo.url}" width="120" '
                f'style="border-radius: 10%;" />')

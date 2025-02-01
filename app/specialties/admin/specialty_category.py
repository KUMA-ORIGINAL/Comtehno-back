from django.contrib import admin
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _

from unfold.admin import ModelAdmin as UnfoldModelAdmin
from unfold.decorators import display

from specialties.models import SpecialtyCategory


@admin.register(SpecialtyCategory)
class SpecialtyCategory(UnfoldModelAdmin):
    list_display = ('id', 'name', 'display_photo')
    list_display_links = ('id', 'name',)

    @display(description=_("Фото"))
    def display_photo(self, obj):
        if obj.photo:
            return mark_safe(
                f'<img src="{obj.photo.url}" height="120" width="120" '
                f'style="border-radius: 10%;" />')

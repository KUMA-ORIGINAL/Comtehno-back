from django.contrib import admin
from .models import FAQ, FAQItem
from unfold.admin import ModelAdmin, TabularInline

class FAQItemInline(TabularInline):  # Встраиваем FAQItem в FAQ
    model = FAQItem
    extra = 1  # Количество пустых форм для добавления новых FAQItem

@admin.register(FAQ)
class FAQAdmin(ModelAdmin):  # исправлено на admin.ModelAdmin
    list_display = ('name',)  # Поля, которые будут отображаться в списке FAQ
    search_fields = ('name',)  # Возможность искать по вопросу
    inlines = [FAQItemInline]  # Вставляем FAQItem как инлайн

@admin.register(FAQItem)
class FAQItemAdmin(ModelAdmin):  # исправлено на admin.ModelAdmin
    list_display = ('question', 'answer')  # Поля, которые будут отображаться в списке FAQItem
    search_fields = ('answer',)  # Возможность искать по ответу


from django.contrib import admin

from .models import MailingList


@admin.register(MailingList)
class MailingListAdmin(admin.ModelAdmin):
    """Рассылка на Email"""
    list_display = ("email", "date")
    search_fields = ("email",)

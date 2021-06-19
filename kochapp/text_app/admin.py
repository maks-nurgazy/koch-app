from django.contrib import admin
from . import models
from .forms import AboutUsForm, PrivacyTextForm


@admin.register(models.AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    form = AboutUsForm


@admin.register(models.PrivacyText)
class PrivacyTextAdmin(admin.ModelAdmin):
    form = PrivacyTextForm

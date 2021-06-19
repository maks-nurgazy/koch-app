from django.contrib import admin
from . import models


@admin.register(models.Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_display = ('name2', 'full_sender_name', 'date_published',)

    def name2(self, obj):
        return obj.name

    name2.short_description = 'Груз'


admin.site.register(models.Transportation)
admin.site.register(models.City)
admin.site.register(models.Region)



from django.contrib import admin

from .models import Config

# Register your models here.
#admin.site.register(Config)

@admin.register(Config)
class ConfigAdmin(admin.ModelAdmin):
    list_display = ['info', "icon", 'color'  ]
    list_display_links = list_display
    list_per_page = 100
    search_fields = ("info", )
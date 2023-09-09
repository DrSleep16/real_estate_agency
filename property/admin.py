from django.contrib import admin

from .models import Flat

@admin.register(Flat)
class FlatModel(admin.ModelAdmin):
    search_fields = ('town', 'address', 'owner')
    readonly_fields = ['created_at']
    list_display = ['town', 'address', 'price', 'new_building', 'construction_year']
    list_editable = ['new_building']

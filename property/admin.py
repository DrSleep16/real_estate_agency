from django.contrib import admin

from .models import Flat

@admin.register(Flat)
class FlatModel(admin.ModelAdmin):
    search_fields = ('town', 'address', 'owner')

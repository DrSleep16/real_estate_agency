# Generated by Django 2.2.24 on 2023-09-09 12:14

from django.db import migrations


def set_new_building_true(apps, schema_editor):
    flat = apps.get_model('property', 'Flat')
    flat.objects.filter(construction_year__gt=2014).update(new_building=True)
    flat.objects.exclude(construction_year__gt=2014).update(new_building=False)


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0003_flat_new_building'),
    ]

    operations = [
        migrations.RunPython(set_new_building_true)
    ]

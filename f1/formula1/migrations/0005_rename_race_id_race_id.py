# Generated by Django 5.0 on 2023-12-24 12:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('formula1', '0004_rename_track_city_track_city_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='race',
            old_name='race_id',
            new_name='id',
        ),
    ]
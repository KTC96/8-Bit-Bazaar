# Generated by Django 3.2.23 on 2024-01-31 15:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0002_auto_20240131_1516'),
    ]

    operations = [
        migrations.RenameField(
            model_name='game',
            old_name='genres',
            new_name='genre',
        ),
    ]

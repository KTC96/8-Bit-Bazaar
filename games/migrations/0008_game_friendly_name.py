# Generated by Django 3.2.23 on 2024-02-02 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0007_auto_20240201_1625'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='friendly_name',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
    ]

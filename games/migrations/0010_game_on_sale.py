# Generated by Django 3.2.23 on 2024-02-08 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0009_alter_game_reviews'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='on_sale',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
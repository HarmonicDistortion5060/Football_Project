# Generated by Django 4.2.1 on 2023-05-20 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('futbol_app', '0002_remove_league_season'),
    ]

    operations = [
        migrations.AddField(
            model_name='league',
            name='season',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
# Generated by Django 2.0.2 on 2018-03-01 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GR', '0003_favorite_toggle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favorite',
            name='toggle',
            field=models.BooleanField(default='False'),
        ),
    ]

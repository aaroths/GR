# Generated by Django 2.0.2 on 2018-03-02 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GR', '0008_intervention_divclass'),
    ]

    operations = [
        migrations.AddField(
            model_name='intervention',
            name='displayorder',
            field=models.IntegerField(default='1'),
        ),
    ]
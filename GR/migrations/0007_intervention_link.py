# Generated by Django 2.0.2 on 2018-03-02 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GR', '0006_auto_20180301_1858'),
    ]

    operations = [
        migrations.AddField(
            model_name='intervention',
            name='link',
            field=models.CharField(default='', max_length=500),
        ),
    ]
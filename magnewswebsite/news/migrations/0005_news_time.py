# Generated by Django 3.0.4 on 2020-04-02 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_auto_20200402_1735'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='time',
            field=models.CharField(default='00:00', max_length=12),
        ),
    ]

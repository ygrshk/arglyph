# Generated by Django 3.1 on 2020-11-07 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('argument', '0003_auto_20201014_2234'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='views',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
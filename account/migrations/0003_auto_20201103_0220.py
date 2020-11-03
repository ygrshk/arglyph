# Generated by Django 3.1 on 2020-11-02 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20201014_2234'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='assets/img', verbose_name='アイコン画像'),
        ),
        migrations.AddField(
            model_name='user',
            name='profile',
            field=models.CharField(blank=True, max_length=150, verbose_name='自己紹介'),
        ),
    ]

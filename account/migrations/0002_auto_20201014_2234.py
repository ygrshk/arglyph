# Generated by Django 3.1 on 2020-10-14 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='メールアドレス'),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=30, verbose_name='姓'),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='名'),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=30, unique=True, verbose_name='ユーザー名'),
        ),
    ]

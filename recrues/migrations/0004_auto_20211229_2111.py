# Generated by Django 3.2.10 on 2021-12-29 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recrues', '0003_auto_20211229_1855'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newrecrue',
            name='cv',
        ),
        migrations.RemoveField(
            model_name='newrecrue',
            name='idcard',
        ),
        migrations.AlterField(
            model_name='newrecrue',
            name='picture',
            field=models.ImageField(upload_to='', verbose_name='image'),
        ),
    ]

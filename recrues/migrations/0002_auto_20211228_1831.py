# Generated by Django 3.2.10 on 2021-12-28 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recrues', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('prenom', models.CharField(max_length=255)),
                ('telephone', models.IntegerField()),
                ('email', models.EmailField(max_length=100)),
                ('ville', models.CharField(max_length=255)),
                ('message', models.CharField(max_length=255)),
                ('usern', models.CharField(max_length=255)),
                ('message_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AlterField(
            model_name='newrecrue',
            name='cv',
            field=models.FileField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='newrecrue',
            name='picture',
            field=models.FileField(blank=True, upload_to=''),
        ),
    ]

# Generated by Django 4.2.7 on 2023-11-07 17:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0002_alter_platformdouyin_avatar'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='platformdouyin',
            name='status',
        ),
    ]
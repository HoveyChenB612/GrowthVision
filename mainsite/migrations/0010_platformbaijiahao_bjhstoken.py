# Generated by Django 4.2.7 on 2023-11-27 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0009_platformbaijiahao'),
    ]

    operations = [
        migrations.AddField(
            model_name='platformbaijiahao',
            name='bjhstoken',
            field=models.CharField(default=None, max_length=500, verbose_name='授权cookies'),
        ),
    ]

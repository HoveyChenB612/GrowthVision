# Generated by Django 4.2.7 on 2023-12-02 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0011_platformdata'),
    ]

    operations = [
        migrations.AddField(
            model_name='platformdata',
            name='nickname',
            field=models.CharField(default=0, max_length=64, verbose_name='用户昵称'),
            preserve_default=False,
        ),
    ]

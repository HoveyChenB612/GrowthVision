# Generated by Django 4.2.7 on 2023-11-22 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0003_platformzhihu'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='platformzhihu',
            name='id',
        ),
        migrations.AlterField(
            model_name='platformzhihu',
            name='zh_uid',
            field=models.BigIntegerField(primary_key=True, serialize=False, verbose_name='知乎用户ID'),
        ),
    ]

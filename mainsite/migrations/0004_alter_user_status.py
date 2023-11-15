# Generated by Django 4.2.7 on 2023-11-09 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0003_remove_platformdouyin_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='status',
            field=models.SmallIntegerField(choices=[(0, '禁用'), (1, '正常')], default=1, verbose_name='状态'),
        ),
    ]
# Generated by Django 4.2.7 on 2023-12-18 08:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0017_alter_platformdata_platform_sensitivewords'),
    ]

    operations = [
        migrations.AlterField(
            model_name='platformbaijiahao',
            name='auth_time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='授权时间'),
        ),
        migrations.AlterField(
            model_name='platformbilibili',
            name='auth_time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='授权时间'),
        ),
        migrations.AlterField(
            model_name='platformdouyin',
            name='auth_time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='授权时间'),
        ),
        migrations.AlterField(
            model_name='platformzhihu',
            name='auth_time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='授权时间'),
        ),
    ]

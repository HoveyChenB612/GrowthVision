# Generated by Django 4.2.7 on 2023-12-18 08:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0018_alter_platformbaijiahao_auth_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historydate',
            name='uid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainsite.user', verbose_name='用户ID'),
        ),
    ]
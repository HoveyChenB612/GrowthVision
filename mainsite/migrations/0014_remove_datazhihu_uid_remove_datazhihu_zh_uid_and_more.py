# Generated by Django 4.2.7 on 2023-12-04 09:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0013_alter_platformdata_item_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='datazhihu',
            name='uid',
        ),
        migrations.RemoveField(
            model_name='datazhihu',
            name='zh_uid',
        ),
        migrations.DeleteModel(
            name='DataDouYin',
        ),
        migrations.DeleteModel(
            name='DataZhiHu',
        ),
    ]
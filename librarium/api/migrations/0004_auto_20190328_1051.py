# Generated by Django 2.1.7 on 2019-03-28 10:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20190327_1238'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='userpic',
            new_name='avatar',
        ),
    ]

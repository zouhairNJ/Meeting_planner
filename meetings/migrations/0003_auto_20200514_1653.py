# Generated by Django 3.0.6 on 2020-05-14 16:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meetings', '0002_auto_20200508_1337'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='x',
            new_name='room_number',
        ),
    ]

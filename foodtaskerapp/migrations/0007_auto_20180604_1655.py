# Generated by Django 2.0.5 on 2018-06-04 14:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foodtaskerapp', '0006_auto_20180512_1420'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='create_at',
            new_name='created_at',
        ),
    ]

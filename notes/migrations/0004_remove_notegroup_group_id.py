# Generated by Django 3.2.5 on 2021-07-20 21:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0003_notegroup_group_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notegroup',
            name='group_id',
        ),
    ]

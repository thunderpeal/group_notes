# Generated by Django 3.2.5 on 2021-08-26 18:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0003_remove_customuser_group_admin'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='note_group',
        ),
    ]
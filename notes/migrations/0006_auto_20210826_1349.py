# Generated by Django 3.2.5 on 2021-08-26 13:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('notes', '0005_groupcolor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='snote',
            name='is_for_group',
        ),
        migrations.AddField(
            model_name='notegroup',
            name='admin',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='snote',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='notes.notegroup'),
        ),
    ]
# Generated by Django 3.2.5 on 2021-08-28 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0014_auto_20210828_2330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membership',
            name='color',
            field=models.CharField(blank=True, default='fdd663', max_length=6, null=True),
        ),
    ]
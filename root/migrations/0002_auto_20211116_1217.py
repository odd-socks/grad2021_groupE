# Generated by Django 2.2.2 on 2021-11-16 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('root', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='root',
            name='lat',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='root',
            name='lon',
            field=models.FloatField(),
        ),
    ]

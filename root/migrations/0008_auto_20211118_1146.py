# Generated by Django 2.2.2 on 2021-11-18 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('root', '0007_auto_20211118_1009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facility',
            name='address',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='user',
            name='address',
            field=models.CharField(max_length=150),
        ),
    ]

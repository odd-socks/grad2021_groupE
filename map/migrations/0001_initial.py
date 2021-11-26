# Generated by Django 2.2.2 on 2021-11-26 01:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Facility',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=150)),
            ],
            options={
                'verbose_name_plural': 'Facility',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=150)),
                ('facility', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='map.Facility')),
            ],
            options={
                'verbose_name_plural': 'User',
            },
        ),
    ]
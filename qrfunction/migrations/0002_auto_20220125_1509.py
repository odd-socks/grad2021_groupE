# Generated by Django 2.2.2 on 2022-01-25 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qrfunction', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarryLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('email', models.EmailField(max_length=254, verbose_name='メールアドレス')),
            ],
        ),
        migrations.AlterModelOptions(
            name='qrfunction',
            options={'verbose_name_plural': 'qrfunction'},
        ),
    ]

# Generated by Django 2.2.2 on 2022-01-24 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0004_auto_20220118_0609'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.EmailField(default=1, max_length=254, verbose_name='メールアドレス'),
            preserve_default=False,
        ),
    ]
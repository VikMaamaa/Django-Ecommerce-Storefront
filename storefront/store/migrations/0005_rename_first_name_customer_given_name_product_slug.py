# Generated by Django 4.1.7 on 2023-03-19 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_auto_20230319_0253'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='first_name',
            new_name='given_name',
        ),
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.TextField(default='-'),
        ),
    ]

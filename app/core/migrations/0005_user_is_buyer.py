# Generated by Django 2.1.15 on 2020-08-10 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_address_financialdetails'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_buyer',
            field=models.BooleanField(default=True),
        ),
    ]

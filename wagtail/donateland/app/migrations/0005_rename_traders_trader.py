# Generated by Django 3.2.8 on 2021-11-07 07:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_traders'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Traders',
            new_name='Trader',
        ),
    ]

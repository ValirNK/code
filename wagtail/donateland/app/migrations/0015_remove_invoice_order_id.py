# Generated by Django 3.2.9 on 2021-11-20 22:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_auto_20211121_0121'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invoice',
            name='order_id',
        ),
    ]

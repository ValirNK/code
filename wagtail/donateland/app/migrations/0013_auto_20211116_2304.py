# Generated by Django 3.2.9 on 2021-11-16 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_auto_20211116_2005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='btcvalue',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='received',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
# Generated by Django 3.2.9 on 2021-11-23 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_remove_invoice_order_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='next_payment',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]

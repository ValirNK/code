# Generated by Django 3.2.8 on 2021-11-07 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_transaction_json'),
    ]

    operations = [
        migrations.CreateModel(
            name='Traders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(max_length=50)),
                ('nick', models.CharField(max_length=50)),
            ],
        ),
    ]
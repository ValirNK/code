# Generated by Django 3.2.8 on 2021-11-09 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_rename_traders_trader'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.CharField(max_length=200)),
                ('json', models.JSONField(blank=True, null=True)),
            ],
        ),
    ]

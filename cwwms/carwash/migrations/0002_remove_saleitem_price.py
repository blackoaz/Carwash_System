# Generated by Django 4.0.4 on 2022-05-12 06:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carwash', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='saleitem',
            name='price',
        ),
    ]
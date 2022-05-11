# Generated by Django 4.0.4 on 2022-05-11 05:05

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carwash', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vehicle',
            old_name='unique_id',
            new_name='uid',
        ),
        migrations.RenameField(
            model_name='vehicle',
            old_name='update_at',
            new_name='updated_at',
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='registration',
            field=models.CharField(max_length=10, unique=True, validators=[django.core.validators.RegexValidator(message="Vehicle Registration doesn't comply", regex='^[A-Z]{2,4}[0-9]{3,4}[A-Z]{1}$')]),
        ),
    ]

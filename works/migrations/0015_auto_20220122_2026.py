# Generated by Django 3.0.1 on 2022-01-22 20:26

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('works', '0014_delete_is_sold'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_rating', models.DecimalField(blank=True, decimal_places=2, default=1, max_digits=3, null=True, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)])),
            ],
        ),
        migrations.AddField(
            model_name='work',
            name='user_rating',
            field=models.DecimalField(blank=True, decimal_places=2, default=1, max_digits=3, null=True, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)]),
        ),
    ]

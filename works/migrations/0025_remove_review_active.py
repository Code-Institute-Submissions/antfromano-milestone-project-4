# Generated by Django 3.0.1 on 2022-02-24 15:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('works', '0024_review_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='active',
        ),
    ]
# Generated by Django 3.0.1 on 2022-02-20 16:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('works', '0013_remove_review_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='date',
        ),
    ]
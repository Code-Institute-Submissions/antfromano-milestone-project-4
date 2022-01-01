# Generated by Django 3.2 on 2022-01-01 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('works', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('description', models.TextField()),
                ('rating', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
            ],
            options={
                'verbose_name_plural': 'Works',
            },
        ),
        migrations.RemoveField(
            model_name='works',
            name='content',
        ),
        migrations.DeleteModel(
            name='Content',
        ),
        migrations.DeleteModel(
            name='Works',
        ),
    ]

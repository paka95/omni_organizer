# Generated by Django 4.1.7 on 2023-04-12 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='content',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='note',
            name='title',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
# Generated by Django 3.1.1 on 2020-12-22 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mypages', '0005_vocabularysets_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vocabularysets',
            name='title',
            field=models.CharField(default='', max_length=20),
        ),
    ]
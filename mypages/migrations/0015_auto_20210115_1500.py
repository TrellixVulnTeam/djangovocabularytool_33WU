# Generated by Django 3.1.1 on 2021-01-15 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mypages', '0014_auto_20201223_2133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vocabularysets',
            name='username',
            field=models.CharField(max_length=50, null=True),
        ),
    ]

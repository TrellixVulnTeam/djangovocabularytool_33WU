# Generated by Django 3.1.1 on 2020-12-23 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mypages', '0010_auto_20201223_2050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vocab',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]

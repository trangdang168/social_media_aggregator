# Generated by Django 3.2.4 on 2021-06-09 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='headline',
            name='id',
        ),
        migrations.AlterField(
            model_name='headline',
            name='url',
            field=models.TextField(primary_key=True, serialize=False),
        ),
    ]

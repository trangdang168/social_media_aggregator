# Generated by Django 3.2.4 on 2021-06-10 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20210609_1638'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='webpage',
            name='id',
        ),
        migrations.AlterField(
            model_name='webpage',
            name='url',
            field=models.URLField(primary_key=True, serialize=False),
        ),
    ]
# Generated by Django 4.2.3 on 2023-08-15 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp1', '0005_leave'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='leave',
            name='check_attendance',
        ),
        migrations.AddField(
            model_name='leave',
            name='check_leave',
            field=models.BooleanField(default=False),
        ),
    ]

# Generated by Django 4.2.3 on 2023-08-15 15:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp1', '0006_remove_leave_check_attendance_leave_check_leave'),
    ]

    operations = [
        migrations.RenameField(
            model_name='leave',
            old_name='check_leave',
            new_name='sanction_leave',
        ),
    ]
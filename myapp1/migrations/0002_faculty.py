# Generated by Django 4.2.3 on 2023-07-28 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tec_id', models.IntegerField()),
                ('tec_name', models.CharField(default=False, max_length=250)),
                ('subject', models.CharField(max_length=250)),
                ('salary', models.CharField(max_length=250)),
            ],
        ),
    ]

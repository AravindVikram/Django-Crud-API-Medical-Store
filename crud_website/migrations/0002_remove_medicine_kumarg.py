# Generated by Django 4.1.7 on 2023-03-23 09:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crud_website', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='medicine',
            name='kumarg',
        ),
    ]

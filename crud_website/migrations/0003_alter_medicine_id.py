# Generated by Django 4.1.7 on 2023-03-23 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud_website', '0002_remove_medicine_kumarg'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicine',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]

# Generated by Django 4.1.7 on 2023-04-17 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud_website', '0003_alter_medicine_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicine',
            name='name',
            field=models.CharField(db_column='name', max_length=100, null=True),
        ),
    ]
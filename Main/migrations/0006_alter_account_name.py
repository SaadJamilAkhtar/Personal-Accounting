# Generated by Django 4.0.1 on 2022-01-23 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0005_remove_entry_counter_remove_entry_type_entry_credit_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]
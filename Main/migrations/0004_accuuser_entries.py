# Generated by Django 4.0.1 on 2022-01-23 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0003_alter_account_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='accuuser',
            name='entries',
            field=models.ManyToManyField(to='Main.Entry'),
        ),
    ]
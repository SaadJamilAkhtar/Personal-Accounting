# Generated by Django 4.0.1 on 2022-01-23 20:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0002_remove_account_credit_remove_account_debit'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='counter',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Main.entry'),
            preserve_default=False,
        ),
    ]

# Generated by Django 5.0.1 on 2024-03-22 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0007_remove_sales_profit_loss'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sales',
            name='receivable_amt',
            field=models.IntegerField(default=0),
        ),
    ]

# Generated by Django 5.0.1 on 2024-03-22 02:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0008_alter_sales_receivable_amt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sales',
            name='grand_total',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='sales',
            name='tax',
            field=models.IntegerField(default=0),
        ),
    ]

# Generated by Django 4.2.7 on 2024-01-25 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sales',
            name='total_price',
            field=models.IntegerField(default=0),
        ),
    ]
# Generated by Django 4.2.4 on 2023-08-22 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderdetail',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]
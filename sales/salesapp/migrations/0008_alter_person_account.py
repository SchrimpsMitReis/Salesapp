# Generated by Django 5.1.2 on 2024-10-31 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salesapp', '0007_bill_product_person_account_order_producttype_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='account',
            field=models.FloatField(blank=True, null=True),
        ),
    ]

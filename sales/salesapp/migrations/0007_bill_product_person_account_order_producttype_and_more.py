# Generated by Django 5.1.2 on 2024-10-30 12:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salesapp', '0006_alter_person_email_addess'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_amount', models.FloatField()),
                ('is_paid', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('price', models.FloatField()),
            ],
        ),
        migrations.AddField(
            model_name='person',
            name='account',
            field=models.FloatField(blank=True, default='', null=True),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bill', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='salesapp.bill')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='salesapp.person')),
            ],
        ),
        migrations.CreateModel(
            name='ProductType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_name', models.CharField(max_length=300)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='salesapp.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='salesapp.product')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='products',
            field=models.ManyToManyField(through='salesapp.ProductType', to='salesapp.product'),
        ),
    ]
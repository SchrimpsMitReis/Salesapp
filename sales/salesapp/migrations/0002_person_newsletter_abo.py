# Generated by Django 5.1.2 on 2024-10-28 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salesapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='newsletter_abo',
            field=models.BooleanField(default=True),
        ),
    ]
# Generated by Django 5.1.2 on 2024-10-30 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salesapp', '0004_remove_person_email_addess'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='email_addess',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
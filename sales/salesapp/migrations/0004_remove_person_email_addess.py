# Generated by Django 5.1.2 on 2024-10-30 06:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('salesapp', '0003_person_email_addess'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='email_addess',
        ),
    ]

# Generated by Django 4.0.1 on 2022-01-27 21:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_rename_created_at_profile_created_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='created',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='updated',
            new_name='updated_at',
        ),
    ]

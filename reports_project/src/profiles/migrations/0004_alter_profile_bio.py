# Generated by Django 4.0.1 on 2022-02-01 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_rename_created_profile_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.TextField(blank=True, default='no bio', max_length=500),
        ),
    ]

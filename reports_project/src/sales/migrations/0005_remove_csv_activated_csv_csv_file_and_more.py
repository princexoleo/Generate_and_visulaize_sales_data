# Generated by Django 4.0.1 on 2022-01-31 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0004_alter_sale_total_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='csv',
            name='activated',
        ),
        migrations.AddField(
            model_name='csv',
            name='csv_file',
            field=models.FileField(null=True, upload_to='csvs/'),
        ),
        migrations.AlterField(
            model_name='csv',
            name='file_name',
            field=models.CharField(max_length=120),
        ),
    ]

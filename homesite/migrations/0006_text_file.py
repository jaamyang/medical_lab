# Generated by Django 2.0 on 2018-03-19 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homesite', '0005_auto_20180318_1721'),
    ]

    operations = [
        migrations.AddField(
            model_name='text',
            name='file',
            field=models.FileField(null=True, upload_to='uploads/'),
        ),
    ]
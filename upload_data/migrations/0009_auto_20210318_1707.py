# Generated by Django 3.1.6 on 2021-03-18 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload_data', '0008_auto_20210318_1650'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificate',
            name='qr_code_size_x',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='certificate',
            name='qr_code_size_y',
            field=models.IntegerField(default=1),
        ),
    ]
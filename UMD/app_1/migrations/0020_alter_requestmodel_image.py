# Generated by Django 4.0.3 on 2022-04-12 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_1', '0019_alter_donationmodel_medicine_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requestmodel',
            name='image',
            field=models.FileField(blank=True, default='/static/13.jpg', null=True, upload_to=''),
        ),
    ]
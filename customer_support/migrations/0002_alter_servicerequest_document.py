# Generated by Django 4.2.11 on 2024-04-20 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer_support', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicerequest',
            name='document',
            field=models.FileField(blank=True, null=True, upload_to='gas_service/documents/%Y/%m/%d/'),
        ),
    ]
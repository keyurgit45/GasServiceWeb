# Generated by Django 4.2.11 on 2024-04-21 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer_support', '0006_alter_servicerequest_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicerequest',
            name='document',
            field=models.FileField(blank=True, null=True, upload_to='images/'),
        ),
    ]
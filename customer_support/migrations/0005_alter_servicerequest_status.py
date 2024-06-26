# Generated by Django 4.2.11 on 2024-04-20 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer_support', '0004_servicerequest_customer_su_service_940ce6_idx_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicerequest',
            name='status',
            field=models.CharField(choices=[('OPEN', 'Open'), ('IN-PROGRESS', 'In-Progress'), ('CLOSED', 'Closed')], default='OPEN', max_length=15),
        ),
    ]

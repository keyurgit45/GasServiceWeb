# Generated by Django 4.2.11 on 2024-04-20 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer_support', '0003_alter_servicerequest_document'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='servicerequest',
            index=models.Index(fields=['service_type'], name='customer_su_service_940ce6_idx'),
        ),
        migrations.AddIndex(
            model_name='servicerequest',
            index=models.Index(fields=['status'], name='customer_su_status_33d8f5_idx'),
        ),
        migrations.AddIndex(
            model_name='servicerequest',
            index=models.Index(fields=['id'], name='customer_su_id_65d844_idx'),
        ),
    ]
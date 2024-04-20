from django.db import models
from django.contrib.auth.models import User

class ServiceRequest(models.Model):
    SERVICE_CHOICES = [
        ('GAS_LEAK', 'Gas Leak'),
        ('BILLING_QUERY', 'Billing Query'),
        ('SERVICE_START', 'Start Service'),
        ('SERVICE_STOP', 'Stop Service'),
        ('OTHER', 'Other'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    service_type = models.CharField(max_length=20, choices=SERVICE_CHOICES)
    description = models.TextField()
    document = models.FileField(upload_to='documents/%Y/%m/%d/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    resolved_at = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=10, default='OPEN', choices=(('OPEN', 'Open'), ('CLOSED', 'Closed')))

    class Meta:
        indexes = [
            models.Index(fields=['service_type']),
            models.Index(fields=['status']),
            models.Index(fields=['id']),
        ]
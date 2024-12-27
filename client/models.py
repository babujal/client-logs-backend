from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class ClientLogs(models.Model):
    client_name = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    gate_code = models.CharField(max_length=200)
    Coments = models.CharField(max_length=800)
    user=models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="WorkOrder")

from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Miner(models.Model):
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    hash_rate = models.CharField(max_length=50)
    power_consumption = models.CharField(max_length=50)
    image = models.ImageField(upload_to='miners/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Transaction(models.Model):
    miner = models.ForeignKey(Miner, on_delete=models.CASCADE)
    buyer = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Transaction for {self.miner.name}"
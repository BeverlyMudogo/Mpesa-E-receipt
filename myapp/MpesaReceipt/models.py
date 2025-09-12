from django.db import models

# Create your models here.
class MpesaTransaction(models.Model):
    transaction_id = models.CharField(max_length=20, unique=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    recipient = models.CharField(max_length=100, null=True, blank=True)
    date = models.DateField(blank=True, null=True)
    time = models.CharField(max_length=20)
    raw_message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.transaction_id} - {self.recipient}"
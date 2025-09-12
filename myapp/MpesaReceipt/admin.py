from django.contrib import admin
from .models import MpesaTransaction

# Register your models here.
@admin.register(MpesaTransaction)
class MpesaTransactionAdmin(admin.ModelAdmin):
    list_display = ("transaction_id", "amount", "recipient", "date", "time", )

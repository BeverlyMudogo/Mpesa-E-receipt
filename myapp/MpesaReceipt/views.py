from .forms import MpesaPaymentForm
from django.shortcuts import render
import re

def manual_sms_input(request):
    context = {}
    context['form'] = MpesaPaymentForm()
    return render(request, 'myapp/sms_input.html', context)

def parse_mpesa_message(request):
    
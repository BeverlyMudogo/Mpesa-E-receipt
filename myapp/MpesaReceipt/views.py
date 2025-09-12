from .forms import MpesaPaymentForm
from django.shortcuts import render, redirect
from .MpesaParser import parse_mpesa_message
from .models import MpesaTransaction

from django.shortcuts import get_object_or_404
from django.http import FileResponse
from .utils import generate_mpesa_receipt

def manual_sms_input(request):
    if request.method == "POST":
        form = MpesaPaymentForm(request.POST)
        if form.is_valid():
            raw_message = form.cleaned_data["Mpesa_sms_field"]

            # Parse the SMS message
            data = parse_mpesa_message(raw_message)

            # Only save if parsing worked
            if data["transaction_id"]:
                transaction=MpesaTransaction.objects.create(
                    transaction_id=data["transaction_id"],
                    amount=data["amount"],
                    recipient=data["recipient"],
                    date=data["date"],
                    time=data["time"],
                    raw_message=raw_message,
                )

            # Redirect after saving
            return render(request, "myapp/success.html", {"transaction": transaction})
    else:
        form = MpesaPaymentForm()

    context = {"form": form}
    return render(request, "myapp/sms_input.html", context)

def download_receipt(request, transaction_id):
    transaction = get_object_or_404(MpesaTransaction, pk=transaction_id)
    pdf_buffer = generate_mpesa_receipt(transaction)

    return FileResponse(pdf_buffer, as_attachment=True, filename=f"receipt_{transaction.transaction_id}.pdf")
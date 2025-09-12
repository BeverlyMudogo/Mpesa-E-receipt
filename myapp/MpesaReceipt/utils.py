from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from io import BytesIO
from django.http import HttpResponse

def generate_mpesa_receipt(transaction):
    # Create in-memory file
    buffer = BytesIO()
    p = canvas.Canvas(buffer, pagesize=A4)

    # Header
    p.setFont("Helvetica-Bold", 16)
    p.drawString(100, 800, "M-PESA Payment Receipt")

    # Transaction details
    p.setFont("Helvetica", 12)
    p.drawString(100, 760, f"Transaction ID: {transaction.transaction_id}")
    p.drawString(100, 740, f"Amount: Ksh {transaction.amount}")
    p.drawString(100, 720, f"Recipient: {transaction.recipient}")
    p.drawString(100, 700, f"Date: {transaction.date}")
    p.drawString(100, 680, f"Time: {transaction.time}")
    p.drawString(100, 660, f"Balance: Ksh {transaction.balance}")
    p.drawString(100, 640, f"Transaction Cost: Ksh {transaction.transaction_cost}")

    # Footer
    p.setFont("Helvetica-Oblique", 10)
    p.drawString(100, 600, "This is a system-generated receipt. Thank you for using our service.")

    # Finalize
    p.showPage()
    p.save()

    buffer.seek(0)
    return buffer

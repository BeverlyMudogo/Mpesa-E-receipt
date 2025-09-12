import re
from datetime import datetime

def parse_mpesa_message(message):
    data = {
        "transaction_id": None,
        "amount": None,
        "recipient": None,
        "date": None,
        "time": None,
        "balance": None,
        "transaction_cost": None,
    }

    # Transaction ID
    match = re.search(r"([A-Z0-9]{10,12})", message)
    if match:
        data["transaction_id"] = match.group(1)

    # Amount
    match = re.search(r"Ksh([\d,]+\.\d{2})", message)
    if match:
        data["amount"] = float(match.group(1).replace(",", ""))

    # Recipient (e.g., PAID TO John Doe or Sent to XYZ)
    match = re.search(r"(?:Sent to|Paid to|Buy goods to|Withdraw to)\s+(.+?)(?:\s+on|\s+for|\s+at|,|\.|$)", message, re.IGNORECASE)
    if match:
        data["recipient"] = match.group(1).strip()

    # Date (e.g., 12/9/25)
    match = re.search(r"(\d{1,2}/\d{1,2}/\d{2})", message)
    if match:
        try:
            data["date"] = datetime.strptime(match.group(1), "%d/%m/%y").date()
        except ValueError:
            data["date"] = None

    # Time (optional, e.g., 10:35 AM)
    match = re.search(r"(\d{1,2}:\d{2}\s?(?:AM|PM))", message, re.IGNORECASE)
    if match:
        data["time"] = match.group(1)

    # Balance (e.g., Balance is Ksh1,234.56)
    match = re.search(r"Balance.*Ksh([\d,]+\.\d{2})", message, re.IGNORECASE)
    if match:
        data["balance"] = float(match.group(1).replace(",", ""))

    # Transaction cost (e.g., Transaction cost, Ksh15.00)
    match = re.search(r"cost[, ]+Ksh([\d,]+\.\d{2})", message, re.IGNORECASE)
    if match:
        data["transaction_cost"] = float(match.group(1).replace(",", ""))

    return data

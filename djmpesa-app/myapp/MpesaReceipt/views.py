# mpesa/views.py
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json

@csrf_exempt
def validation_url(request):
    if request.method == "POST":
        data = json.loads(request.body.decode('utf-8'))
        print("Validation request:", data)

        # Example: only accept if BillRefNumber is not empty
        if data.get("BillRefNumber"):
            return JsonResponse({"ResultCode": 0, "ResultDesc": "Accepted"})
        else:
            return JsonResponse({"ResultCode": 1, "ResultDesc": "Rejected"})
    return JsonResponse({"error": "Invalid request"}, status=400)


@csrf_exempt
def confirmation_url(request):
    if request.method == "POST":
        data = json.loads(request.body.decode('utf-8'))
        print("Confirmation request:", data)

        # TODO: Save to your DB here
        return JsonResponse({"ResultCode": 0, "ResultDesc": "Accepted"})
    return JsonResponse({"error": "Invalid request"}, status=400)

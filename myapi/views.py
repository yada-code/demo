from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from .models import License
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt  # ไม่ให้ตรวจสอบ CSRF Token (สำหรับ API)
def send_message(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            uuid = data.get("uuid")
            license_key = data.get("license_key")
            # พิมพ์ค่าหรือเก็บข้อมูลลงในฐานข้อมูลตามต้องการ
            print(f"Received uuid: {uuid}, license_key: {license_key}")
            return JsonResponse({"status": "Message received successfully"})
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)
    return JsonResponse({"error": "Only POST requests allowed"}, status=405)
from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse, HttpResponse
from .models import License
from django.views.decorators.csrf import csrf_exempt
import json
def home(request):
    return HttpResponse("Welcome to the homepage!")

# ฟังก์ชันสำหรับรับ payload
@csrf_exempt
def receive_payload(request):
    if request.method == "POST":
        try:
            # อ่านข้อมูลจาก payload
            data = json.loads(request.body)
            uuid = data.get("uuid")
            license_key = data.get("license_key")

            # บันทึกข้อมูลลงฐานข้อมูล (แก้ไขตาม fields ใน models.py ของคุณ)
            license_entry = License(uuid=uuid, license_key=license_key)
            license_entry.save()

            return JsonResponse({"status": "success", "message": "Payload received and saved"})
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)}, status=400)
    else:
        return JsonResponse({"status": "error", "message": "Only POST requests are allowed"}, status=405)
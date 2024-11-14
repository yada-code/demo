from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from .models import License
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt  # ไม่ให้ตรวจสอบ CSRF Token (สำหรับ API)
def register_license(request):
    if request.method == 'POST':
        # รับค่าจาก API
        try:
            data = json.loads(request.body)
            uuid = data.get('uuid')
            license_key = data.get('license_key')

            # บันทึกข้อมูลในฐานข้อมูล
            if uuid and license_key:
                license = License(uuid=uuid, license_key=license_key)
                license.save()
                return JsonResponse({'status': 'success', 'message': 'License saved successfully'})
            else:
                return JsonResponse({'status': 'error', 'message': 'Missing uuid or license_key'}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({'status': 'error', 'message': 'Invalid JSON'}, status=400)
    return JsonResponse({'status': 'error', 'message': 'Only POST requests are allowed'}, status=405)


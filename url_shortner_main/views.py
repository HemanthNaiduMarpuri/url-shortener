from django.shortcuts import render
from url_qr.models import QrCode

def homeview(request):
    qr_list = QrCode.objects.all().order_by('-created_at')[:10]
    context = {
        'qr_list':qr_list
    }
    return render(request, 'home.html', context)
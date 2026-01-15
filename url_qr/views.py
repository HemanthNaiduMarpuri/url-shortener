from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
import qrcode
import io
from .models import QrCode
from django.core.files.base import ContentFile

@login_required
def create_qrcode(request):
    context = {}
    if request.method == 'POST':
        url = request.POST.get('url')
        if url:
            qr_code = qrcode.make(url)
            buffer = io.BytesIO()
            qr_code.save(buffer, format='PNG')

            qr_instance = QrCode.objects.create(
                user=request.user,
                url=url
            )

            qr_instance.qrcode.save(
                f"qr_{qr_instance.id}.png",
                ContentFile(buffer.getvalue()),
                save=True
            )
            context['qr'] = qr_instance
    return render(request, 'qrcode/create_qrcode.html',context)

@login_required
def qrcode_list(request):
    user = request.user
    qr_list = QrCode.objects.filter(user=user).order_by('-created_at')
    context = {
        'qr_list':qr_list
    }
    return render(request, 'qrcode/qrcode_list.html', context)

@login_required
def qrcode_detail(request, qr_id):
    user = request.user
    qr_detail = get_object_or_404(QrCode, id=qr_id, user=user)

    context = {
        'qr_detail':qr_detail
    }

    return render(request, 'qrcode/qrcode_detail.html', context)





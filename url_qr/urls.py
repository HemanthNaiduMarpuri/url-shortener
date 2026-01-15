from django.urls import path
from .views import qrcode_detail, qrcode_list, create_qrcode

urlpatterns = [
    path('create/', create_qrcode, name='create_qrcode'),
    path('list/', qrcode_list, name='qrcode_list'),
    path('detail/<int:qr_id>/', qrcode_detail, name='qrcode_detail')
]

from django.db import models
from url_users.models import Users
from datetime import timedelta
from django.utils import timezone

class QrCode(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='user_qrcode')
    url = models.CharField(max_length=1024)
    qrcode = models.ImageField(upload_to='qr_code/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()

    def save(self, *args, **kwargs):
        if not self.expires_at:
            if self.user:
                self.expires_at = timezone.now() + timedelta(days=30)
            else:
                self.expires_at = timezone.now() + timedelta(days=7)
        return super().save(*args, **kwargs)
    
    def is_expired(self):
        return timezone.now() > self.expires_at
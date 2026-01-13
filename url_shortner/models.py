from django.db import models
from url_users.models import Users
from datetime import timedelta
from django.utils import timezone

class ShortUrl(models.Model):
    short_key = models.CharField(max_length=10, unique=True)
    long_url = models.TextField()
    user = models.ForeignKey(Users, null=True, blank=True, on_delete=models.SET_NULL)
    session_token = models.CharField(max_length=64, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()
    click_count = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.expires_at:
            if self.user:
                self.expires_at = timezone.now() + timedelta(days=30)
            else:
                self.expires_at = timezone.now() + timedelta(days=7)
        super().save(*args, **kwargs)

    def is_expired(self):
        if not self.expires_at:
            return True
        return self.expires_at <= timezone.now()




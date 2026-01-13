from django.urls import path
from .views import create_short_url, user_url_list, user_url_detail

urlpatterns = [
    path('create/', create_short_url, name='create_short_url'),
    path('url-list/', user_url_list, name='user_urls'),
    path('url-detail/<int:url_id>/', user_url_detail, name='url_detail')
]

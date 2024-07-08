# urls.py
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('blogs/', views.all_blogs, name='all_blogs'),
    path('blogs/<int:blog_id>/', views.blog_details, name='blog_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

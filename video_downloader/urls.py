"""
URL configuration for video_downloader project.
"""


from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('downloader_app.urls')),
]

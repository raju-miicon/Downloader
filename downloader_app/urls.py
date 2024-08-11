from django.urls import path


from downloader_app import views

urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.search_video, name='search_video'),
    path('download/', views.download_video, name='download_video'),
]

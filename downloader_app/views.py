from django.shortcuts import render

# Create your views here.


from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from pytube import YouTube
import yt_dlp
import os


import json
from django.http import JsonResponse, HttpResponse
import yt_dlp
import os



def home(request):
    return render(request, 'downloader/home.html')

def search_video(request):
    url = request.GET.get('url')
    video_info = None

    # Use yt-dlp for downloading from multiple platforms
    ydl_opts = {
        'quiet': True,
        'skip_download': True,
        'format': 'best',
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        video_info = ydl.extract_info(url, download=False)
    
    return JsonResponse({
        'title': video_info.get('title'),
        'thumbnail': video_info.get('thumbnail'),
        'formats': [{'format_id': f['format_id'], 'resolution': f['resolution'], 'filesize': f.get('filesize')} for f in video_info.get('formats') if f.get('filesize')]
    })


def download_video(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            url = data.get('url')
            format_id = data.get('format_id')

            # Debugging print statements
            print(f"URL: {url}")
            print(f"Format ID: {format_id}")

            if not url or not format_id:
                return JsonResponse({"error": "Invalid URL or format ID"}, status=400)

            ydl_opts = {
                'format': format_id,
                'outtmpl': os.path.join('downloads', '%(title)s.%(ext)s'),
            }

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            
            return JsonResponse({"message": "Download Successful"}, status=200)
        
        except Exception as e:
            print(f"Error: {str(e)}")
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"error": "Invalid request"}, status=400)
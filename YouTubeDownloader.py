import yt_dlp


ydl_opts = {
    'format': 'best',
    'outtmpl': 'indirilen_video.%(ext)s',
}

def download_video(url):
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

video_url = input("Enter video URL: ")

download_video(video_url)

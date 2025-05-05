import os
from pytube import YouTube

def download_youtube_video(url, audio_only=False):
    """
    Download video or audio from YouTube.
    :param url: YouTube URL to download.
    :param audio_only: Flag to download audio only (True) or video (False).
    :return: None
    """
    try:
        # Creating YouTube object
        yt = YouTube(url)
        
        if audio_only:
            # Download audio only (best audio stream)
            print("🔄 Downloading audio...")
            stream = yt.streams.filter(only_audio=True).first()
            stream.download(output_path="downloads", filename=f"{yt.title}.mp3")
            print(f"✅ Audio downloaded: {yt.title}.mp3")
        else:
            # Download video (best video stream)
            print("🔄 Downloading video...")
            stream = yt.streams.get_highest_resolution()
            stream.download(output_path="downloads", filename=f"{yt.title}.mp4")
            print(f"✅ Video downloaded: {yt.title}.mp4")
    
    except Exception as e:
        print(f"❌ Error: {e}")

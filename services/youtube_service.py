import os
from pytube import YouTube
from config.config import TEMP_DOWNLOAD_PATH

class YouTubeDownloader:
    def __init__(self):
        os.makedirs(TEMP_DOWNLOAD_PATH, exist_ok=True)
    
    async def download_audio(self, url: str) -> str:
        try:
            yt = YouTube(url)
            audio_stream = yt.streams.filter(only_audio=True).first()
            
            # Download audio
            output_path = os.path.join(TEMP_DOWNLOAD_PATH, f"{yt.video_id}.mp3")
            audio_stream.download(filename=output_path)
            
            return output_path
            
        except Exception as e:
            raise Exception(f"Failed to download YouTube video: {str(e)}")
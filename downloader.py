import os
import yt_dlp

VIDEO_URL = " " 
COOKIES_FILE = "cookies.txt"  
OUTPUT_DIR = "./downloads" 

# In case of 3h vids, you can set download speed limit by `--limit-rate 5M` for network stability

def download_video():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    ydl_opts = {
        'cookiefile': COOKIES_FILE,     
        'outtmpl': os.path.join(OUTPUT_DIR, '%(title)s.%(ext)s'),
        'retries': 10,  # retries for network error
        'fragment_retries': 10,
        'http_chunk_size': 10485760, 
        'progress_hooks': [progress_hook],  # progress bar
        'concurrent_fragment_downloads': 8,  # parallel download
        'throttledratelimit': 5000000, 
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([VIDEO_URL])
        print("Success!")
    except Exception as e:
        print(f"Err. : {e}")

def progress_hook(d):
    if d['status'] == 'downloading':
        # Progress bar
        progress = d.get('_percent_str', "?")
        speed = d.get('_speed_str', "?")
        eta = d.get('_eta_str', "?")
        print(f"\rcompletion rate: {progress} | speed: {speed}/s | ETA: {eta}", end='', flush=True)

if __name__ == "__main__":
    print("Download start")
    print(f"target: {VIDEO_URL}")
    download_video()

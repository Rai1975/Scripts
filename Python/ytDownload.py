# In the future, this will be updated to download video/audio from any client
import yt_dlp

def download_youtube_video_as_mp3(youtube_url, output_folder=r"C:\Users\User\Music\Downloads"):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': f'{output_folder}/%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',  
        }],
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([youtube_url])
        print("Download and conversion to MP3 complete!")
    except Exception as e:
        print(f"An error occurred: {e}")

def download_video(url, output_path=r"C:\Users\User\Videos\Downloads"):
    ydl_opts = {
        'format': 'best',
        'outtmpl': f'{output_path}/%(title)s.%(ext)s',
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

youtube_url = input("Enter the YouTube video URL: ")
choice = int(input("MP3 / MP4 (0/1): "))

if choice == 0:
    download_youtube_video_as_mp3(youtube_url)
elif choice == 1:
    download_video(youtube_url)
else:
    print("Invalid choice.")
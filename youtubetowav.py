from __future__ import unicode_literals
import yt_dlp
import sys

ydl_opts = {
    'format': 'bestaudio/best',
    'cookies': 'cookies.txt',  # Replace with the path to your cookies.txt
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'wav',
    }],
}

def download_from_url(url):
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

if __name__ == '__main__':
    args = sys.argv[1:]
    if len(args) > 1:
        print("Too many arguments.")
        print("Usage: python youtubetowav.py <optional link>")
        print("If a link is given it will automatically convert it to .wav. Otherwise a prompt will be shown.")
        exit()
    if len(args) == 0:
        url = input("Enter YouTube URL: ")
        download_from_url(url)
    else:
        download_from_url(args[0])

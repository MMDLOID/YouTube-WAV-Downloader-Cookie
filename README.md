# YouTube-WAV-Downloader

## Overview
This Python script allows you to download YouTube videos as high-quality WAV audio files. It is simple to use and generates files compatible with applications like [FM Transmitter](https://github.com/markondej/fm_transmitter), making it ideal for broadcasting, audio processing, or personal projects.

## Features
- Downloads YouTube videos as audio files in WAV format.
- Ensures high-quality audio output.
- Easy-to-use command-line interface.

## Prerequisites
Before using this script, ensure you have the following:
- Python 3.8 or higher.
- Required Python libraries:
  - `yt-dlp` (for downloading YouTube videos)
  - `ffmpeg` (for audio processing)

To install the dependencies, run:
```bash
pip install yt-dlp
```
Make sure `ffmpeg` is installed on your system and accessible via the command line. For installation instructions, visit [FFmpeg.org](https://ffmpeg.org/download.html).

## Installation
1. Clone this repository or download the script:
   ```bash
   git clone https://github.com/yourusername/YouTube-WAV-Downloader.git
   cd YouTube-WAV-Downloader
   ```
2. Place the script (`YouTube_to_WAV.py`) in a directory of your choice.

## Usage
To download a YouTube video as a WAV file, use the following command:
```bash
python YouTube_to_WAV.py <YouTube URL>
```
### Example
```bash
python YouTube_to_WAV.py https://www.youtube.com/watch?v=aqz-KE-bpKQ
```

### Notes:
- If no URL is provided, the script will prompt you to enter one interactively.
- The output WAV file will be saved in the same directory as the script.

## Troubleshooting
### Common Issues
- **"Signature extraction failed" or similar errors**:
  - Ensure you have the latest version of `yt-dlp` by running:
    ```bash
    pip install -U yt-dlp
    ```
  - If the issue persists, use a cookies file for authentication (see below).

### Using a Cookies File
Some YouTube videos may require authentication. To resolve this:
1. Install the [Get Cookies.txt]([https://chrome.google.com/webstore/detail/get-cookiestxt/fldmcdmbojjnaeibddoooagecekgkaac](https://chromewebstore.google.com/detail/get-cookiestxt-locally/cclelndahbckbenkjhflpdbgdldlbecc)) browser extension.
2. Export your YouTube cookies and save them as `cookies.txt` in the same directory as the script.
3. Modify the script's `ydl_opts` to include:
   ```python
   'cookies': 'cookies.txt',
   ```

## Acknowledgments
- [yt-dlp](https://github.com/yt-dlp/yt-dlp) for YouTube video downloading.
- [FFmpeg](https://ffmpeg.org) for powerful audio processing.


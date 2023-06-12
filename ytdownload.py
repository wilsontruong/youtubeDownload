import os
from pytube import YouTube
import time

start_time = time.time()

# Create directories for videos and audios
videoDir = 'C:/Users/wlsn1/Desktop/Youtube Videos/Videos'
clipsDir = 'C:/Users/wlsn1/Desktop/Youtube Videos/Clips'
audioDir = 'C:/Users/wlsn1/Desktop/Youtube Videos/Songs'
soundDir = 'C:/Users/wlsn1/Desktop/Youtube Videos/Sound Effects'

if not os.path.exists(videoDir):
    os.mkdir(videoDir)
if not os.path.exists(audioDir):
    os.mkdir(audioDir)

selection = input(
    "Do you want to download a song or a Youtube video?: Select 1 for videos, 2 for video clips, 3 for songs, or 4 for sound effects: ")

while (selection != '1' and selection != '2' and selection != '3' and selection != '4'):
    selection = input(
        "Invalid number, pick 1 for videos, 2 for video clips, 3 for songs, or 4 for sound effects: ")

url = input("Enter Your Link: ")
# create a YouTube object2
yt = YouTube(url)

if selection == '1':
    # get the video and audio stream and download them
    print("Video is currently downloading...")
    yt.streams.get_highest_resolution().download(
        output_path=videoDir, filename_prefix='video')

if selection == '2':
    # get the video and audio stream and download them
    print("Clip is currently downloading...")
    yt.streams.get_highest_resolution().download(
        output_path=clipsDir, filename_prefix='video')

elif selection == '3':
    # get the videos stream and download it
    print("Song is currently downloading...")
    audio = yt.streams.filter(only_audio=True).first()
    audio.download(audioDir)

elif selection == '4':
    # get the videos stream and download it
    print("Sound effect is currently downloading...")
    soundEffect = yt.streams.filter(only_audio=True).first()
    soundEffect.download(soundDir)

end_time = time.time()
elapsed_time = end_time - start_time
print(f"This download took: {elapsed_time} seconds to download.")

import os
import time
from tkinter import Tk, Label, Entry, Button, OptionMenu, messagebox, StringVar
from pytube import YouTube

# Function to handle download process


def download_process():
    url = entry.get()
    selection = option.get()

    if selection == "Video":
        output_dir = videoDir
        filename_prefix = 'video'
        message = "Video is currently downloading..."
    elif selection == "Video Clip":
        output_dir = clipsDir
        filename_prefix = 'video'
        message = "Clip is currently downloading..."
    elif selection == "Song":
        output_dir = audioDir
        filename_prefix = None
        message = "Song is currently downloading..."
    elif selection == "Sound Effect":
        output_dir = soundDir
        filename_prefix = None
        message = "Sound effect is currently downloading..."

    try:
        yt = YouTube(url)
        start_time = time.time()

        if filename_prefix:
            yt.streams.get_highest_resolution().download(
                output_path=output_dir, filename_prefix=filename_prefix)
        else:
            audio = yt.streams.filter(only_audio=True).first()
            audio.download(output_dir)

        end_time = time.time()
        elapsed_time = end_time - start_time
        messagebox.showinfo(
            "Download Complete", f"This download took: {elapsed_time} seconds to complete.")
    except Exception as e:
        messagebox.showerror(
            "Download Failed", f"An error occurred:\n{str(e)}")


# Create directories for videos and audios
# CHANGE THESE DIRECTORIES TO WHERE YOU WANT TO STORE IT! MAKE SURE IT IS A STRING!
videoDir = ''
clipsDir = ''
audioDir = ''
soundDir = ''

if not os.path.exists(videoDir):
    os.makedirs(videoDir)
if not os.path.exists(audioDir):
    os.makedirs(audioDir)

# Create the main window
window = Tk()
window.title("YouTube Downloader")
window.geometry("400x200")
window.resizable(False, False)

# Create the input label and entry field
label_url = Label(window, text="Enter YouTube Link:")
label_url.pack(pady=10)
entry = Entry(window, width=50)
entry.pack(pady=5)

# Create the selection label and option menu
label_option = Label(window, text="Select Download Type:")
label_option.pack()
option = StringVar(window)
option.set("Video")  # Default value is set to 'Video'
menu = OptionMenu(window, option, "Video",
                  "Video Clip", "Song", "Sound Effect")
menu.pack(pady=5)

# Create the download button
button = Button(window, text="Download", command=download_process)
button.pack(pady=10)

# Run the GUI main loop
window.mainloop()

import tkinter
import customtkinter
from pytube import YouTube

def onProgress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    completed_percentage = bytes_downloaded / total_size * 100
    percentage = str(int(completed_percentage))
    progress_percentage.configure(text=percentage + "%")
    progress_percentage.update()

    # update progress bar
    progress_bar.set(float(completed_percentage) / 100)


def startDownload():
    try:
        # reset texts
        title.configure(text="")
        download_status.configure(title="")

        ytLink = link.get()
        ytObject = YouTube(ytLink, on_progress_callback=onProgress)
        video = ytObject.streams.get_highest_resolution()
        title.configure(text=ytObject.title)
        video.download()
        download_status.configure(text="Download completed")
    except:
        download_status.configure(text="Error downloading video", text_color="red")

# System settings
customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("blue")

# App frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("YouTube Downloader")

# UI elements
title = customtkinter.CTkLabel(app, text="Insert a youtube link")
title.pack(padx=10, pady=10)

download_status = customtkinter.CTkLabel(app, text="")
download_status.pack()

# Link input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack(padx=10, pady=10)

# Download button
download = customtkinter.CTkButton(app, text="Download", command=startDownload, text_color="white")
download.pack(padx=10, pady=10)

# Download progress
progress_percentage = customtkinter.CTkLabel(app, text="0%")
progress_percentage.pack()

progress_bar = customtkinter.CTkProgressBar(app, width=400)
progress_bar.set(0)
progress_bar.pack(padx=10, pady=10)

# Run app
app.mainloop()
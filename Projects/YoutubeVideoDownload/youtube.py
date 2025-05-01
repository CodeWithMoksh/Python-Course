# Imports the YouTube class from the pytubefix module. This class is used to interact with a YouTube video (fetch info, download, etc.).
from pytubefix import YouTube

#  Imports a progress callback function that shows a progress bar or percentage when a download is in progress.
from pytubefix.cli import on_progress

# Asks the user for a YouTube video link and removes any extra spaces with .strip().
url = input("Enter the link of your video: ").strip()

# Creates a YouTube object using the entered URL and attaches the on_progress function to show download progress.
try:
    yt = YouTube(url, on_progress_callback=on_progress) #This object now lets you access metadata (title, views, etc.) or download the video.
except Exception as e:
    print("Error loading video:", e)
    exit()

print("""
1 - Title
2 - Description
3 - Views
4 - Chapters
5 - Captions
6 - Channel URL
7 - Likes
8 - Download
""")

try:
    user = int(input("Tell us what do you want from this: "))
except ValueError:
    print("Please enter a valid number.")
    exit()

if user == 1:
    print("Title:", yt.title)

elif user == 2:
    print("Description:", yt.description)

elif user == 3:
    print("Views:", yt.views)

elif user == 4:
    print("Chapters:", yt.chapters)

elif user == 5:
    print("Available Captions:")
    for caption in yt.captions:
        print(" -", caption)

elif user == 6:
    print("Channel URL:", yt.channel_url)

elif user == 7:
    print("Likes:", yt.likes)

elif user == 8:
    # Finds the stream with the highest video resolution that includes both video and audio.
    ys = yt.streams.get_highest_resolution()

    # Downloads the stream and stores the file path where it's saved.
    path = ys.download()

    # Shows that the video has been downloaded and to this path 
    print(f"Success! Video saved to: {path}")

else:
    print("Invalid input.")

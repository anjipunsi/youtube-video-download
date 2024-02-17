from pytube import YouTube

# YouTube video URL
url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

# Create a YouTube object
yt = YouTube(url)

# Get the highest resolution stream
stream = yt.streams.get_highest_resolution()

# Download the video
stream.download()

print("Download sucessfully")

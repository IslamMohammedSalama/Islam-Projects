'''the module clac to items'''

def add(a , b=0) -> float:

    '''that add the arge mts'''
    return float(a + b)

def sudscript(a , b=0) -> float:

    '''that sudscript the argemts'''
    return float(a - b)

def malit(a , b=0) -> float:

    '''that malit the argemts'''
    return float(a * b)

def delvid(a , b=0) -> float:

    '''that add the argemts'''
    if b == 0 :
        raise ZeroDivisionError
    return float(a / b)

from pytube import YouTube

# Replace 'video_link' with the actual YouTube video link
video_link = 'https://www.youtube.com/watch?v=nzN6ihvwFN8'

# Create a YouTube object
yt = YouTube(video_link)

# Get the highest resolution video stream
video_stream = yt.streams.get_highest_resolution()

# Download the video
video_stream.download()

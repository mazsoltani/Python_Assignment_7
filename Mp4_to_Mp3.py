import os
from moviepy.editor import *
mp4_file = r'D:\film.mp4'
mp3_file = r'D:\film.mp3'
videoclip = VideoFileClip(mp4_file)
audioclip = videoclip.audio
audioclip.write_audiofile(mp3_file)
audioclip.close()
videoclip.close()


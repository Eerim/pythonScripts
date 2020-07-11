import moviepy.editor
from moviepy.editor import *

# get video from file
video = VideoFileClip("videoplayback.mp4")

# convert video to webm
video.write_videofile("videoplayback.webm", fps=25)

# rotate 180°
rotatedVideo = video.rotate(180)
rotatedVideo.write_videofile("rotated_videoplayback.mp4", fps=25)

# crop 80th second to 150th second
croppedVideo = video.subclip(80, 150)
croppedVideo.write_videofile("cropped_videoplayback.mp4", fps=25)

# reduce audio x 0.5
reducedvolumeVideo = video.volumex(0.5)
reducedvolumeVideo.write_videofile("reducedvolume_videoplayback.mp4", fps=25)

# get audio file
audio = video.audio
audio.write_audiofile("videoplayback.mp3")

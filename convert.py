from moviepy import editor

video = editor.VideoFileClip("karimi1400.mp4")
audio = video.audio
audio.write_audiofile("karimi1400.mp3")
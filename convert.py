from moviepy import editor

video = editor.videoFileClip("karimi1400.mp4")
video.audio.write_audiofile("karimi1400.mp4")
CALL activate machine_learning
 python video_writer.py
 ffmpeg -i fractal_light.avi -i audio.flac -codec copy -shortest output.avi
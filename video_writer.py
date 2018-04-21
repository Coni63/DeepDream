import cv2
import os
from PIL import Image

dream_name = 'fractal_light'
dream_path = 'dream/{}'.format(dream_name)

i = 0
while True:
    if os.path.isfile('dream/{}/img_{}.jpg'.format(dream_name, i)):
        if i == 0:
            image = Image.open('dream/{}/img_{}.jpg'.format(dream_name, i))
            width, height = image.size
            del image
        i += 1
    else:
        dream_length = i
        break
        
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('{}.avi'.format(dream_name),fourcc, 30.0, (width, height))
        
for i in range(dream_length):
    img_path = os.path.join(dream_path,'img_{}.jpg'.format(i))
    frame = cv2.imread(img_path)
    out.write(frame)

out.release()
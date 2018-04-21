'''
Some info on various layers, so you know what to expect
depending on which layer you choose:

layer 1: wavy
layer 2: lines
layer 3: boxes
layer 4: circles?
layer 5: heads
layer 6: dogs, bears, cute animals.
layer 7: snakes, buildings
layer 8: fish begin to appear, frogs/reptilian eyes.
layer 9 : fish, snake, turtles
layer 10: Monkies, lizards, snakes, duck
layer 11: birds

Choosing various parameters like num_iterations, rescale,
and num_repeats really varies on which layer you're doing.


We could probably come up with some sort of formula. The
deeper the layer is, the more iterations and
repeats you will want.

Layer 3: 20 iterations, 0.5 rescale, and 8 repeats is decent start
Layer 10: 40 iterations and 25 repeats is good.
'''
from deepdreamer import model, load_image, recursive_optimize
import numpy as np
import PIL.Image
import cv2
import os
import random
import sys
import itertools
import math
import shutil

dream_name = 'fractal_light'

if os.path.isfile('dream/{}/img_0.jpg'.format(dream_name)):
    img_result = load_image(filename='dream/{}/img_0.jpg'.format(dream_name))
    x_size = img_result.shape[1]
    y_size = img_result.shape[0]
    brightness_avg = np.mean(img_result) 
else:
    print("Missing image for this dream")
    sys.exit()

created_count = 0
max_count = 30 * (60 + 57) # 1 min 57 @ 30 fps

cycle_color = itertools.cycle([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
cycle_layer = itertools.cycle([5, 7, 9, 11, 6, 8, 10])

while True:

    if created_count > max_count:
        break

    if created_count == 0:  # up to 3.5s
        # set the layer to use until next change
        layer_tensor = model.layer_tensors[2]

        # Number of iteration :  the deeper we go, the more we need
        num_iterations = 1

        # Update how fast we zoom in ( higher => slower )
        zoom_speed = 512
        x_trim = x_size // zoom_speed
        y_trim = y_size // zoom_speed

        # Update balance of color (RGB format).
        # If sum == 1 : brighness is maintained
        # If sum > 1 : brighness increase
        # If sum < 1 : brighness decrease
        color_balance = [0.5, 0.5, 0.0]   # yellow - electrical sound
    elif created_count == 3.5*30: # up to 4.3s
        layer_tensor = model.layer_tensors[7]

        num_iterations = 20

        zoom_speed = 256
        x_trim = x_size // zoom_speed
        y_trim = y_size // zoom_speed

        color_balance = [0.2, 0.2, 0.6]
    elif created_count == 4.3*30: # up to 6s
        layer_tensor = model.layer_tensors[8]

        num_iterations = 20

        zoom_speed = 256
        x_trim = x_size // zoom_speed
        y_trim = y_size // zoom_speed

        color_balance = [0.6, 0.2, 0.2]
    elif created_count == 6*30: # up to 6.5s
        layer_tensor = model.layer_tensors[3]

        num_iterations = 5

        zoom_speed = 350
        x_trim = x_size // zoom_speed
        y_trim = y_size // zoom_speed

        color_balance = [0.4, 0.4, 0.2]
    elif created_count == 6.5*30: # up to 7s
        layer_tensor = model.layer_tensors[2]

        num_iterations = 5

        zoom_speed = 512
        x_trim = x_size // zoom_speed
        y_trim = y_size // zoom_speed

        color_balance = [0.35, 0.35, 0.35]
    elif created_count == 7*30: # up to 8s
        layer_tensor = model.layer_tensors[3]

        num_iterations = 5

        zoom_speed = 512
        x_trim = x_size // zoom_speed
        y_trim = y_size // zoom_speed

        color_balance = [0.33, 0.33, 0.33]
    elif created_count == 8*30: # up to 9s
        layer_tensor = model.layer_tensors[9]

        num_iterations = 40

        zoom_speed = 128
        x_trim = x_size // zoom_speed
        y_trim = y_size // zoom_speed

        color_balance = [0.25, 0.35, 0.4]
    elif created_count == 9*30: # up to 10s
        layer_tensor = model.layer_tensors[10]

        num_iterations = 40

        zoom_speed = 256
        x_trim = x_size // zoom_speed
        y_trim = y_size // zoom_speed

        color_balance = [0.25, 0.35, 0.4]
    elif created_count == 10 * 30:  # up to 11s
        layer_tensor = model.layer_tensors[2]

        num_iterations = 5

        zoom_speed = 512
        x_trim = x_size // zoom_speed
        y_trim = y_size // zoom_speed

        color_balance = [0.33, 0.33, 0.33]
    elif created_count == 11 * 30:  # up to 13s
        layer_tensor = model.layer_tensors[3]

        num_iterations = 10

        zoom_speed = 512
        x_trim = x_size // zoom_speed
        y_trim = y_size // zoom_speed

        color_balance = [0.30, 0.30, 0.30]
    elif created_count == 13 * 30:  # up to 13.5s
        layer_tensor = model.layer_tensors[4]

        num_iterations = 10

        zoom_speed = 256
        x_trim = x_size // zoom_speed
        y_trim = y_size // zoom_speed

        color_balance = [0.20, 0.20, 0.60]
    elif created_count == 13.5 * 30:  # up to 14.9s
        layer_tensor = model.layer_tensors[7]

        num_iterations = 10

        zoom_speed = 256
        x_trim = x_size // zoom_speed
        y_trim = y_size // zoom_speed

        color_balance = [0.40, 0.37, 0.37]
    elif created_count == 14.9 * 30:  # up to 15.6s
        layer_tensor = model.layer_tensors[7]

        num_iterations = 10

        zoom_speed = 256
        x_trim = x_size // zoom_speed
        y_trim = y_size // zoom_speed

        color_balance = [0.37, 0.31, 0.31]
    elif created_count == 15.6 * 30:  # up to 19.9s
        layer_tensor = model.layer_tensors[7]

        num_iterations = 15

        zoom_speed = 512
        x_trim = x_size // zoom_speed
        y_trim = y_size // zoom_speed

        color_balance = [0.34, 0.33, 0.33]
    elif created_count == 19.9 * 30:  # up to 25.6s
        layer_tensor = model.layer_tensors[8]

        num_iterations = 20

        zoom_speed = 400
        x_trim = x_size // zoom_speed
        y_trim = y_size // zoom_speed

        color_balance = [0.30, 0.25, 0.40]
    elif created_count == 25.6 * 30:  # up to 26.5s
        layer_tensor = model.layer_tensors[8]

        num_iterations = 30

        zoom_speed = 400
        x_trim = x_size // zoom_speed
        y_trim = y_size // zoom_speed
        color_balance = [0.5, 0.5, 0.1]
    elif created_count == 26.5 * 30:  # up to 28.6s
        layer_tensor = model.layer_tensors[3]

        num_iterations = 20

        zoom_speed = 400
        x_trim = x_size // zoom_speed
        y_trim = y_size // zoom_speed
        color_balance = [0.4, 0.3, 0.3]
    elif created_count == 28.6 * 30:  # up to 31s
        layer_tensor = model.layer_tensors[7]

        num_iterations = 15

        zoom_speed = 512
        x_trim = x_size // zoom_speed
        y_trim = y_size // zoom_speed

        color_balance = [0.34, 0.33, 0.33]
    elif created_count == 31 * 30:  # up to 32.5s
        layer_tensor = model.layer_tensors[4]

        num_iterations = 10

        zoom_speed = 128
        x_trim = x_size // zoom_speed
        y_trim = y_size // zoom_speed

        color_balance = [0.34, 0.33, 0.33]
    elif created_count == 32.5 * 30:  # up to 33.5s
        layer_tensor = model.layer_tensors[7]

        num_iterations = 15

        zoom_speed = 512
        x_trim = x_size // zoom_speed
        y_trim = y_size // zoom_speed

        color_balance = [0.34, 0.33, 0.33]
    elif created_count == 33.5 * 30: 
        layer_tensor = model.layer_tensors[8]

        num_iterations = 20

        zoom_speed = 256
        x_trim = x_size // zoom_speed
        y_trim = y_size // zoom_speed

        color_balance = [0.6, 0.2, 0.2]
    elif created_count == 36 * 30:
        layer_tensor = model.layer_tensors[3]

        num_iterations = 20

        zoom_speed = 512
        x_trim = x_size // zoom_speed
        y_trim = y_size // zoom_speed

        color_balance = [0.32, 0.34, 0.34]
    elif created_count == 43.1 * 30:
        layer_tensor = model.layer_tensors[3]

        num_iterations = 20

        zoom_speed = 512
        x_trim = x_size // zoom_speed
        y_trim = y_size // zoom_speed

        color_balance = [0.33, 0.33, 0.33]
    elif created_count == 44.1 * 30:
        layer_tensor = model.layer_tensors[2]

        num_iterations = 10

        zoom_speed = 512
        x_trim = x_size // zoom_speed
        y_trim = y_size // zoom_speed

        color_balance = [0.33, 0.33, 0.33]
    elif created_count == 44.9 * 30:
        layer_tensor = model.layer_tensors[3]

        num_iterations = 15

        zoom_speed = 512
        x_trim = x_size // zoom_speed
        y_trim = y_size // zoom_speed

        color_balance = [0.33, 0.33, 0.33]
    elif created_count == 45.7 * 30:
        layer_tensor = model.layer_tensors[1]

        num_iterations = 10

        zoom_speed = 512
        x_trim = x_size // zoom_speed
        y_trim = y_size // zoom_speed

        color_balance = [0.33, 0.33, 0.33]
    elif created_count == 46.7 * 30:
        layer_tensor = model.layer_tensors[2]

        num_iterations = 10

        zoom_speed = 512
        x_trim = x_size // zoom_speed
        y_trim = y_size // zoom_speed

        color_balance = [0.33, 0.33, 0.33]
    elif created_count == 47.5 * 30:
        layer_tensor = model.layer_tensors[3]

        num_iterations = 15

        zoom_speed = 512
        x_trim = x_size // zoom_speed
        y_trim = y_size // zoom_speed

        color_balance = [0.33, 0.33, 0.33]
    elif created_count == 48.5 * 30:
        layer_tensor = model.layer_tensors[1]

        num_iterations = 10

        zoom_speed = 512
        x_trim = x_size // zoom_speed
        y_trim = y_size // zoom_speed

        color_balance = [0.4, 0.3, 0.3]
    elif created_count == 52.6 * 30:
        layer_tensor = model.layer_tensors[2]

        num_iterations = 20

        zoom_speed = 350
        x_trim = x_size // zoom_speed
        y_trim = y_size // zoom_speed

        color_balance = [0.2, 0.6, 0.2]
    elif created_count == 53.7 * 30:
        layer_tensor = model.layer_tensors[3]

        num_iterations = 15

        zoom_speed = 512
        x_trim = x_size // zoom_speed
        y_trim = y_size // zoom_speed

        color_balance = [0.2, 0.2, 0.6]
    elif created_count >= 54.7 * 30 and  created_count < 62.3 * 30:
        zoom_speed = 256
        x_trim = x_size // zoom_speed
        y_trim = y_size // zoom_speed
        if (created_count - (54.7 * 30)) % 13 == 0:
            layer_tensor = model.layer_tensors[next(cycle_layer)]
            color_balance = next(cycle_color)
    elif created_count >= 62.3 * 30 and  created_count < 75.9 * 30:
        zoom_speed = 256
        x_trim = x_size // zoom_speed
        y_trim = y_size // zoom_speed
        if (created_count - (54.7 * 30)) % 24 == 0:
            layer_tensor = model.layer_tensors[next(cycle_layer)]
            color_balance = next(cycle_color)
    elif created_count >= 75.9 * 30 and created_count < 89.6 * 30:
        zoom_speed = 256
        x_trim = x_size // zoom_speed
        y_trim = y_size // zoom_speed
        if (created_count - (54.7 * 30)) % 36 == 0:
            layer_tensor = model.layer_tensors[next(cycle_layer)]
            color_balance = next(cycle_color)
    elif created_count == 89.6 * 30:
        zoom_speed = 256
        x_trim = x_size // zoom_speed
        y_trim = y_size // zoom_speed
        num_iterations = 10
        layer_tensor = model.layer_tensors[2]
        color_balance = [0, 0.5, 0.5]
    elif created_count == 93 * 30:
        zoom_speed = 256
        x_trim = x_size // zoom_speed
        y_trim = y_size // zoom_speed
        num_iterations = 20
        layer_tensor = model.layer_tensors[8]
        color_balance = [0.34, 0.33, 0.33]
    elif created_count == 96.5 * 30:
        zoom_speed = 256
        x_trim = x_size // zoom_speed
        y_trim = y_size // zoom_speed
        num_iterations = 40
        layer_tensor = model.layer_tensors[11]
        color_balance = [0.34, 0.33, 0.33]
    elif created_count == 102.5 * 30:
        zoom_speed = 256
        x_trim = x_size // zoom_speed
        y_trim = y_size // zoom_speed
        num_iterations = 15
        layer_tensor = model.layer_tensors[3]
        color_balance = [0.33, 0.34, 0.33]
    elif created_count >= 105.2 * 30 and  created_count < 110.4 * 30:
        zoom_speed = 256 + (created_count - (105.2 * 30))
        x_trim = int(x_size // zoom_speed)
        y_trim = int(y_size // zoom_speed)
        num_iterations = 15
        layer_tensor = model.layer_tensors[3]
        color_balance = [0.4, 0.4, 0.2]
    elif created_count >= 110.4 * 30:
        req_image = (117-110.4)*30
        image_created = int(110.4 * 30)
        step = int(image_created // req_image)
        for i in range(image_created, 0, -step):
            dst_dir = 'dream/{}/img_{}.jpg'.format(dream_name, created_count+1)
            src_file = 'dream/{}/img_{}.jpg'.format(dream_name, i)
            shutil.copy(src_file, dst_dir)
            created_count += 1
            continue
        break

    if os.path.isfile('dream/{}/img_{}.jpg'.format(dream_name, created_count+1)):
        print('{} already exists, continuing along...'.format(created_count+1))
        created_count += 1
        continue

    img_result = load_image(filename='dream/{}/img_{}.jpg'.format(dream_name, created_count))

    img_result = img_result[0+x_trim:y_size-y_trim, 0+y_trim:x_size-x_trim]
    img_result = cv2.resize(img_result, (x_size, y_size))

    # Use these to modify the general colors and brightness of results.
    # results tend to get dimmer or brighter over time, so you want to
    # manually adjust this over time.
    current_brightness = np.mean(img_result)
    delta = 3* (current_brightness - brightness_avg)
    img_result[:, :, 0] -= color_balance[0] * delta  # reds
    img_result[:, :, 1] -= color_balance[1] * delta  # greens
    img_result[:, :, 2] -= color_balance[2] * delta  # blues

    img_result = np.clip(img_result, 0.0, 255.0)
    img_result = img_result.astype(np.uint8)

    img_result = recursive_optimize(layer_tensor=layer_tensor,
                                    image=img_result,
                                    num_iterations=num_iterations,
                                    step_size=1.0,
                                    rescale_factor=0.7,
                                    num_repeats=1,
                                    blend=0.2)

    img_result = np.clip(img_result, 0.0, 255.0)
    img_result = img_result.astype(np.uint8)
    result = PIL.Image.fromarray(img_result, mode='RGB')
    result.save('dream/{}/img_{}.jpg'.format(dream_name, created_count+1))

    print('image {} created'.format(created_count + 1))

    created_count += 1
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

# This fill select the output folder for images
dream_name = 'fractal_light'

# get the image size and brightness
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
        color_balance = [0.5, 0.5, 0.0]   # yellow move to yellow
    elif created_count == 3.5 * 30:  # 3.5 seconds @ 30 fps
        # You can add additionnal command here ... They are just removed for readability
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
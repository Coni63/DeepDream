# Deep Dream Video

Based on the work of Sentdex on [youtube](https://www.youtube.com/user/sentdex), or on his own [website](https://pythonprogramming.net/). I've re-created the repository used to create DeepDreams. With an audio from [youtube](https://www.youtube.com/watch?v=O5RdMvgk8b0), I've generated an Deep Dream Video available below:

[![movie](https://github.com/Coni63/DeepDream/blob/master/dream/fractal_light/img_0.jpg)](https://www.youtube.com/watch?v=KW3CJ7i6LP4)

## How it works

### What are the parameters

This algorithm is based on inception pre-trained network. You can select the layer you want to apply for the dream. The deeper you go, the more complexe features it creates. We can sum up layer as follow :

* layer 1: wavy
* layer 2: lines
* layer 3: boxes
* layer 4: circles?
* layer 5: heads
* layer 6: dogs, bears, cute animals.
* layer 7: snakes, buildings
* layer 8: fish begin to appear, frogs/reptilian eyes.
* layer 9 : fish, snake, turtles
* layer 10: Monkies, lizards, snakes, duck
* layer 11: birds

And below, you ahve a generated image with every layer :

#### Initial Image
![Initial Image](https://github.com/Coni63/DeepDream/blob/master/img/the-starry-night-800x450.jpg)
#### Layer 1
![Layer 1](https://github.com/Coni63/DeepDream/blob/master/img/dream_image_out_layer_1.jpg)
#### Layer 2
![Layer 2](https://github.com/Coni63/DeepDream/blob/master/img/dream_image_out_layer_2.jpg)
#### Layer 3
![Layer 3](https://github.com/Coni63/DeepDream/blob/master/img/dream_image_out_layer_3.jpg)
#### Layer 4
![Layer 4](https://github.com/Coni63/DeepDream/blob/master/img/dream_image_out_layer_4.jpg)
#### Layer 5
![Layer 5](https://github.com/Coni63/DeepDream/blob/master/img/dream_image_out_layer_5.jpg)
#### Layer 6
![Layer 6](https://github.com/Coni63/DeepDream/blob/master/img/dream_image_out_layer_6.jpg)
#### Layer 7
![Layer 7](https://github.com/Coni63/DeepDream/blob/master/img/dream_image_out_layer_7.jpg)
#### Layer 8
![Layer 8](https://github.com/Coni63/DeepDream/blob/master/img/dream_image_out_layer_8.jpg)
#### Layer 9
![Layer 9](https://github.com/Coni63/DeepDream/blob/master/img/dream_image_out_layer_9.jpg)
#### Layer 10
![Layer 10](https://github.com/Coni63/DeepDream/blob/master/img/dream_image_out_layer_10.jpg)
#### Layer 11
![Layer 11](https://github.com/Coni63/DeepDream/blob/master/img/dream_image_out_layer_11.jpg)

You can also select some other features like :

* num_iterations : Number if iterations between the input and the output. The deeper you are, the more you need to see important changes
* x_trim and y_trim :  modify spped zoom. It removes n_trim pixel on both size at every iteration creating a zoom effect. In my code, I created a variable zoom_speed which calculate N_trim based on the image size. Like thatwe have the same zoom on a small image, 1080p image or 4k image.
* there is few other options I let you dig in (num_repeats, step_size, blend, rescale_factor)

### How to generate images

You can create image simply by using *dream_image.py*. Just modify the layer and the path to the image. There is no color balance as this process applied between 2 images in a video.

### How to generate videos

This is handled in 2 steps :

#### First Step :  create images

To create images, you should run *dream_on.py*. But upfront you have to :

* create a folder into **dream** folder with the name of your dream. Inside, add the initial image called **img_0.jpg**.
* for every timeframe:
  * Select the layer
  * Select the color balance
  * Select the number of iterations
  
 then you can run this script.

#### Second Step :  Render video and add audio (optionnal)

When all images are rendered, you can create the video by running the script *video_writer.py* after having changed the **dream_name**.
If you want to apply a music in the video, use ffmpeg and run the command :

<code>ffmpeg -i path_to_your_video.avi -i path_to_your_audio.mp3/wav/flac -codec copy -shortest path_to_the_output_video.avi</code>

The duration of the output will be the shorter duration of either audio or video.

## Changes

The initial code and the inception module can be found at [this link](https://pythonprogramming.net/static/downloads/machine-learning-data/deep_dreaming_start.zip).

Based on this, I changed :

1. the color balance

Originally, it was only adding +2 to each color layer or add a random value between 2 and 4.

```python

# Before
img_result[:, :, 0] += 2  # reds
img_result[:, :, 1] += 2  # greens
img_result[:, :, 2] += 2  # blues

# or 

img_result[:, :, 0] += random.choice([3, 4])  # reds
img_result[:, :, 1] += random.choice([3, 4])  # greens
img_result[:, :, 2] += random.choice([3, 4])  # blues

# After
# I first save the initial brightness then I just adjust 
current_brightness = np.mean(img_result)
delta = 3* (current_brightness - brightness_avg)
img_result[:, :, 0] -= color_balance[0] * delta  # reds
img_result[:, :, 1] -= color_balance[1] * delta  # greens
img_result[:, :, 2] -= color_balance[2] * delta  # blues

```

2. Some loops
Most of the code should run indefinitely. This was coded using a range and this has been replaced by while True

```python

# Before
for i in range(0, 9999999999999999):
	foo()
	
# After
i = 0
while True:
	foo()
	i += 1
	
```

3. Add a color balance
In order to be able to drive the color balance in the video, you should provide a list of 3 floats which drives the color of the image. This is the <code>color_balance</code> variable you see in the first change 

```python

color_balance = [0.333, 0.333, 0.333]
	
```

* if the sum = 1, brightness will be maintained
* if the sum < 1, brightness decrease exponentially (as we remove X% for the delta which will increase)
* if the sum > 1, brightness increase exponentially too 
* the balance is R, G, B so to change the color balance to red, you can apply [1, 0, 0]

3. add a target color

This is not done yet but the idea would be to drive the color change based on a target. For example, you set that you want the picture to balance to a specific color, the algorithme will detect the proper balance to apply.


## Acknowledgment

** * Sentdex for his [youtube playlist](https://www.youtube.com/watch?v=a7Og0ImTg9Q&list=PLQVvvaa0QuDdfN3lrO0NDYxa1JwCYes-E)
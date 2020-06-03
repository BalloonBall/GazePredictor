# UI tracker test for a single image

import os
import random

from pygaze.defaults import *
from constants import *

from pygaze.display import Display
from pygaze.screen import Screen
from pygaze.eyetracker import EyeTracker
from pygaze.keyboard import Keyboard
from pygaze.time import Time
from pygaze.logfile import Logfile
from pygaze.libtime import clock

from pygaze.plugins.aoi import AOI


# # # # #
# directory stuff

DIR = os.path.split(os.path.abspath(__file__))[0]
image_file = os.path.join(DIR, 'www.google.co.uk_(Pixel 2).png')

# # # # #
# create instances

# initialize the display
disp = Display()

# initialize a screen
scr = Screen()


# initialize an EyeTracker
tracker = EyeTracker(disp)

# initialize a keyboard
kb = Keyboard(keylist=['space'],timeout=None)

# initialize a Timer
timer = Time()

# create a new logfile
log = Logfile(filename="test")
log.write(["x_pos","y_pos", "time"])

# # # # #
# test gaze contingency

# UI test
scr.clear()
scr.draw_image(image_file)
x = (DISPSIZE[0] - IMGSIZE[0]) / 2 # centre minus half of the image width
y = (DISPSIZE[1] - IMGSIZE[1]) / 2 # centre minus half of the image height
aoi = AOI('rectangle', (x,y), IMGSIZE)
disp.fill(scr)
t1 = disp.show()
key = None
tracker.start_recording()
while key != 'space':
    # check for key input
    key, presstime = kb.get_key(keylist=['space'],timeout=1)
    # get gaze position
    gazepos = tracker.sample()
    gazetime = clock.get_time() - t1
    if aoi.contains(gazepos):
        print(gazepos)
        print(gazetime)
        log.write([gazepos[0],gazepos[1],gazetime])
    else:
        continue
tracker.stop_recording()

# # # # #
# close down

# ending screen
scr.clear()

# close
log.close()
tracker.close()
disp.close()
timer.expend()

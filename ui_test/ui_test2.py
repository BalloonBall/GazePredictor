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
from detectors import fixation_detection as fd

# # # # #
# directory stuff

DIR = os.path.split(os.path.abspath(__file__))[0]
image_file = os.path.join(DIR, 'argos.png')

# # # # #
# create instances

# initialize the display
disp = Display()

# initialize a screen
scr = Screen()

# initialize a keyboard
kb = Keyboard(keylist=['space'],timeout=None)

# test gaze contingency

# UI test
scr.clear()
scr.draw_image(image_file)
disp.fill(scr)
t1 = disp.show()
key = None
while key != 'space':
    # check for key input
    key, presstime = kb.get_key(keylist=['space'],timeout=1)

# # # # #
# close down
scr.clear()
disp.close()

# ending screen

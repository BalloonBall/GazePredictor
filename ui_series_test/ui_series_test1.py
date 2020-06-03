

# native
import os
import random

# PyGaze
from constants import *
from pygaze.libscreen import Display, Screen
from pygaze.libinput import Keyboard
from pygaze.eyetracker import EyeTracker
from pygaze.liblog import Logfile
import pygaze.libtime as timer
from pygaze.plugins.aoi import AOI
# # # # #
# SETUP

# visuals
disp = Display()
scr = Screen()

# input
kb = Keyboard()
tracker = EyeTracker(disp)

# output
log = Logfile(filename="test_series")
log.write(["trialnr", "image", "gaze_pos_x", "gaze_pos_y", "gaze_time"])

# # # # #
# PREPARE

# load instructions from file
instfile = open(INSTFILE)
instructions = instfile.read()
instfile.close()

instfile = open(INSTFILE_DC)
instruction_dc = instfile.read()
instfile.close()
# read all image names
images = os.listdir(IMGDIR)
image_size = (555, 987)

# display instructions
scr.draw_text(text="Press any key to start the calibration.", fontsize=TEXTSIZE_L)
disp.fill(scr)
disp.show()

# wait for a keypress
kb.get_key(keylist=None, timeout=None, flush=True)

# calibrate the eye tracker
tracker.calibrate()

# # # # #
# RUN

# display task instructions
scr.clear()
scr.draw_text(text=instructions, fontsize=TEXTSIZE_M)

disp.fill(scr)
disp.show()

# wait for a keypress
kb.get_key(keylist=None, timeout=None, flush=True)

# display drift check instructions
scr.clear()
scr.draw_text(text=instruction_dc, fontsize=TEXTSIZE_M)
disp.fill(scr)
disp.show()

# wait for a keypress
kb.get_key(keylist=None, timeout=None, flush=True)

# loop through all trials
ntrials = len(images)
for trialnr in range(ntrials):
    # PREPARE TRIAL
    # draw the image
    scr.clear()
    scr.draw_image(os.path.join(IMGDIR, images[trialnr]),pos=(DISPSIZE[0] / 2, DISPSIZE[1] / 2))
    x = (DISPSIZE[0] - image_size[0]) / 2  # centre minus half of the image width
    y = (DISPSIZE[1] - image_size[1]) / 2  # centre minus half of the image height
    aoi = AOI('rectangle', (x, y), image_size)
    disp.fill(scr)

    # perform a drift check
    tracker.drift_correction()

    # RUN TRIAL
    # start tracking
    tracker.start_recording()
    tracker.log("TRIALSTART %d" % trialnr)
    tracker.log("IMAGENAME %s" % images[trialnr])
    tracker.status_msg("trial %d/%d" % (trialnr + 1, ntrials))

    # present image
    disp.fill(scr)
    t0 = disp.show()
    tracker.log("image online at %d" % t0)

    # wait for a bit for participant viewing image
    while True:
        gaze_pos = tracker.sample()
        gaze_time = timer.get_time() - t0
        if aoi.contains(gaze_pos):
            print(gaze_pos)
            log.write([trialnr, images[trialnr], gaze_pos[0], gaze_pos[1], gaze_time])
        if timer.get_time()-t0 >= TRIALTIME:
            break

    # reset screen
    disp.fill()
    t1 = disp.show()
    tracker.log("image offline at %d" % t1)

    # stop recording
    tracker.log("TRIALEND %d" % trialnr)
    tracker.stop_recording()

    # inter trial interval
    timer.pause(ITI)

# # # # #
# CLOSE

# loading message
scr.clear()
scr.draw_text(text="Transferring the data file, please wait...", fontsize=TEXTSIZE_M)
disp.fill(scr)
disp.show()

# neatly close connection to the tracker
# (this will close the data file, and copy it to the stimulus PC)
tracker.close()

# close the logfile
log.close()

# exit message
scr.clear()
scr.draw_text(text="This is the end of this experiment. Thank you for participating!\n\n(press any key to exit)",
              fontsize=TEXTSIZE_M)
disp.fill(scr)
disp.show()

# wait for a keypress
kb.get_key(keylist=None, timeout=None, flush=True)

# close the Display
disp.close()

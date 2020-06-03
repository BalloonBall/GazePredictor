import os.path

# FILES AND FOLDERS
# the DIR constant contains the full path to the current directory, which will
# be used to determine where to store and retrieve data files
DIR = os.path.dirname(__file__)
# the IMGDIR is the path to the directory that contains the image files
IMGDIR = os.path.join(DIR, 'imgs')
# the INSTFILE is the path to the file that contains the instructions
INSTFILE = os.path.join(DIR, 'instructions.txt')
INSTFILE_DC = os.path.join(DIR, 'instruction_dc.txt')



# DISPLAY
DISPTYPE = 'pygame'
# the DISPSIZE is the monitor resolution, e.g. (1024,768)
DISPSIZE = (1920,1080)
# the SCREENSIZE is the physical screen size in centimeters, e.g. (39.9,29.9)
SCREENSIZE = (33.2,18.7)
# the SCREENDIST is the distance in centimeters between the participant and the
# display
SCREENDIST = 50.0
# set FULLSCREEN to True for fullscreen displaying, or to False for a windowed
# display
FULLSCREEN = True
# BGC is for BackGroundColour, FGC for ForeGroundColour; both are RGB guns,
# which contain three values between 0 and 255, representing the intensity of
# Red, Green, and Blue respectively, e.g. (0,0,0) for black, (255,255,255) for
# white, or (255,0,0) for the brightest red
BGC = (0,0,0)
FGC = (255,255,255)
# the TEXTSIZE determines the size of the text in the experiment
TEXTSIZE_M = 36
TEXTSIZE_L = 72
IMGSIZE = 405, 720

# TIMING
# the TRIALTIME is the time each image is visible
TRIALTIME = 5000 # ms
TRIALTIME_L = 20000 # ms
# the intertrial interval (ITI) is the minimal amount of time between the
# presentation of two consecutive images
ITI = 2000 # ms

# EYE TRACKING
# the TRACKERTYPE indicates the brand of eye tracker, and should be one of the
# following: 'eyelink', 'smi', 'tobii' 'dumbdummy', 'dummy'
TRACKERTYPE = 'dummy'
# the EYELINKCALBEEP constant determines whether a beep should be sounded on
# the appearance of every calibration target (EyeLink only)
EYELINKCALBEEP = True
# set DUMMYMODE to True if no tracker is attached
DUMMYMODE = False

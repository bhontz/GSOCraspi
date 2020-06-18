# SLIDESHOW PROGRAM (see: https://github/bhontz/GSOCraspi/code/slideshow.py)
import os, pygame, glob
from datetime import datetime

# create our pygame window in the upper left corner of the screen
os.environ['SDL_VIDEO_WINDOW_POS'] = '0,0'

# build up a list of all of the pictures we took TODAY
filePattern = '/home/pi/Pictures/{}*.jpg'.format(datetime.now().strftime("%Y-%b-%d"))
lstFileNames = glob.glob(filePattern)  # this python module creates a list of filenames
lstFileNames.sort()  # sort the list of picture filenames in the order the pictures were taken

if len(lstFileNames) == 0:
    print("ERROR: there aren't any files with this pattern: {}".format(filePattern))

pygame.init()
screen = pygame.display.set_mode((640, 480))  # set the window to the same size as the pictures
pygame.display.set_caption('Photobooth Pics')

for filename in lstFileNames:
    print(filename)
    clock = pygame.time.Clock()
    dt = 0  # capture the change in clock ticks
    timer = 3  # seconds of delay between pictures

    image = pygame.image.load(filename)  # load a picture from the list
    screen.fill((255,255,255))
    screen.blit(image, (0,0))

    while True:
        if timer <= 0:
            break

        for e in pygame.event.get():
            if e in pygame.event.get():
                if e.type == pygame.QUIT:
                    pygame.quit()


        pygame.display.update()
        dt = clock.tick(30) / 1000  # record 1 second since the last clock tick
        timer -= dt

pygame.quit()
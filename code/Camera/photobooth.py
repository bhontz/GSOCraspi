# PHOTOBOOTH PROGRAM (see: https://github/bhontz/GSOCraspi/code/photobooth.py)
import os, pygame
from datetime import datetime
from picamera import PiCamera

# create our pygame window in the upper left corner of the screen
os.environ['SDL_VIDEO_WINDOW_POS'] = '0,0'

pygame.init()
screen = pygame.display.set_mode((240,240)) # size of our pygame window
pygame.display.set_caption('Photobooth')

counter = 5
label = '* {} *'.format(counter)

font = pygame.font.SysFont('Arial Bold', 80)  # set an 80 point font for our countdown
pygame.time.set_timer(pygame.USEREVENT, 1000) # 1000 milliseconds = 1 second

camera = PiCamera()
camera.resolution = '640 x 480' # size of the pictures we'll take
camera.start_preview()

while True:
    for event in pygame.event.get():
        if event.type == pygame.USEREVENT:
            counter = counter - 1
            if counter == 0:
                # next line makes our picture file names look like this: 2020-Jun-03-10-07-32.jpg
                pictureFileName = "/home/pi/Pictures/{}.jpg".format(datetime.now().strftime("%Y-%b-%d-%H-%M-%S"))
                camera.capture(pictureFileName)
                camera.stop_preview()
            else:
                label = '* {} *'.format(counter)
            
        elif event.type == pygame.QUIT:
            counter = 0
            break
            
    if counter == 0:
        break
        
    screen.fill((255,255,255)) # set white background for our pygame window
    # next line sets a black font color and positions our text at 64, 96 within our pygame window
    screen.blit(font.render(label, True, (0, 0, 0)), (64, 96))
    pygame.display.flip()  # this line draws everything
    
camera.close()
pygame.quit()
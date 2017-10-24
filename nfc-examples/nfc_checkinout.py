# NFC Checkin and out
# Developed by Philippe De Pauw - Waterschoot

import nxppy
import logging
import time
import sys, pygame

# Configure logging
logging.basicConfig()

# Connecto to Mifare
mifare = nxppy.Mifare()

# Initialize Pygame
pygame.init()
size = width, height = 320, 240
color_black = 0, 0, 0
color_green = 0, 255, 0
color_red = 255, 0, 0
screen = pygame.display.set_mode(size)
screen.fill(color_black)
pygame.display.update()

# Set for checked-in things
checkedIn = set()

# Print card UIDs as they are detected
while True:
    try:
        uid = mifare.select()
        print("Detected NFC Tag UID: %r" %uid)
        
        if uid in checkedIn:
            checkedIn.remove(uid)
            screen.fill(color_red)
            pygame.display.set_caption("Checkout NFC Tag UID: %r" %uid)
            print("Checkout NFC Tag UID: %r" %uid)
        else:
            checkedIn.add(uid)
            screen.fill(color_green)
            pygame.display.set_caption("Checkin NFC Tag UID: %r" %uid)
            print("Checkin NFC Tag UID: %r" %uid)

        pygame.display.update()

    except nxppy.SelectError:
        # SelectError is raised if no card is in the field.
        pass

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    time.sleep(1)
    
    screen.fill(color_black)
    pygame.display.update()


# NFC Checkin with Mock
# Developed by Philippe De Pauw - Waterschoot

import nxppy
import logging
import time
import datetime
from datetime import timezone
import sys, pygame

# Configure logging
logging.basicConfig()

# Connecto to Mifare
mifare = nxppy.Mifare()

# Initialize Pygame
pygame.init()
size = width, height = 640, 480
color_black = 0, 0, 0
color_green = 0, 255, 0
color_red = 255, 0, 0
screen = pygame.display.set_mode(size)
screen.fill(color_black)
pygame.display.update()

# Person class
class Person:
    def __init__(self, id, firstName, surName, uid, imageURL):
        self.id = id
        self.firstName = firstName
        self.surName = surName
        self.uid = uid
        self.imageURL = imageURL
        self.lastCheckedIn = None

    def check_in(self):
        dt = datetime.datetime.now()
        self.lastCheckedIn = dt.replace(tzinfo=timezone.utc).timestamp()

    def full_name(self):
        return self.firstName + " " + self.surName

# Create persons        
persons = set()
persons.add(Person(1, "Philippe", "De Pauw - Waterschoot", "04BE2D224B3F80", "images/pdp.jpg"))
persons.add(Person(2, "Olivier", "Parent", "043323224B3F81", "images/opr.png"))
persons.add(Person(3, "Kristof", "Raes", "04E60B224B3F80", "images/kr.png"))

# Print card UIDs as they are detected
while True:    
    try:
        uid = mifare.select()
        print("Detected NFC Tag UID: %r" %uid)
        
        for p in persons:
            if p.uid == uid:
                break
        else:
            p = None

        if p is not None:
            p.check_in()
            screen.fill(color_green)
            pygame.display.set_caption("Verified person: %r" %p.full_name())
            personImg = pygame.image.load(p.imageURL)
            screen.blit(personImg, (0, 0))
            pygame.display.update()

    except nxppy.SelectError:
        # SelectError is raised if no card is in the field.
        pass

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    time.sleep(1)
    
    screen.fill(color_black)
    pygame.display.update()

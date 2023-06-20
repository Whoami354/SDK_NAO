import pygame
from naoqi import ALProxy
import naoqi

motion = naoqi.ALProxy("ALMotion", "192.168.171.141", 9559)
motion.setMotionConfig([["ENABLE_FOOT_CONTACT_PROTECTION", True]])
# speech = naoqi.ALProxy("ALTextToSpeech", "192.168.171.151", 9559)
# move = naoqi.ALProxy("ALRobotPosture", "192.168.171.151", 9559)

# speech.setLanguage("German")


# motion.moveTo(0.0, 0.0, 0.0)
# motion.moveTo(0.5, 0.0, 0.0)

# motion.rest()
# speech.say("Ich wache nun auf!")
# speech.say("Hallo Welt!")
# motion.wakeUp()
# speech.say("Ich bin NAO und ich bin mit Gregory verbunden!")

# speech.say("Ich laufe vorwaerts!")
# speech.say("Ich laufe rueckwaerts!")
# motion.moveTo(-0.2, 0, 0, 0)

# speech.say("Ich laufe nach links seitwaerts!")
# motion.moveTo(0, 0.2, 0, -1)
# speech.say("Ich laufe nach rechts seitwaerts!")
# motion.moveTo(0, -0.2, 0, 1)

import pygame
from pygame.locals import *

speed = 1.0

def check_spacebar_pressed():
    pygame.init()
    screen = pygame.display.set_mode((400, 300))
    clock = pygame.time.Clock()

    while True:
        motion.setMotionConfig([["ENABLE_FOOT_CONTACT_PROTECTION", True]])
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                return False
            elif event.type == KEYUP:
                print("Ich bin drinnen")
                motion.stopMove()
            elif event.type == pygame.JOYAXISMOTION:
                print("Controller")
            elif event.type == KEYDOWN and (event.key == K_UP or event.key == K_w):
                print("Es wird auf Pfeiltaste nach oben Gedrueckt")
                motion.setWalkTargetVelocity(speed, 0, 0, 0)
            elif event.type == KEYDOWN and (event.key == K_DOWN or event.key == K_s):
                print("Es wird auf Pfeiltaste nach unten Gedrueckt")
                motion.setWalkTargetVelocity(-speed, 0, 0, 0)
            elif event.type == KEYDOWN and (event.key == K_LEFT or event.key == K_a):
                print("Es wird nach links gelaufen!")
                motion.setWalkTargetVelocity(0, speed, 0, 0)
            elif event.type == KEYDOWN and (event.key == K_RIGHT or event.key == K_d):
                print("Es wird nach recht gelaufen!")
                motion.setWalkTargetVelocity(0, -speed, 0, 0)
            elif event.type == KEYDOWN and event.key == K_l:
                print("Ich rotiere nach links")
                motion.setWalkTargetVelocity(0, 0, speed, 0)
            elif event.type == KEYDOWN and event.key == K_r:
                print("Ich rotiere nach links")
                motion.setWalkTargetVelocity(0, 0, -speed, 0)
        clock.tick(60)


check_spacebar_pressed()

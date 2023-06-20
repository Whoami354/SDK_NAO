import almath
from naoqi import ALProxy

import naoqi

motion = naoqi.ALProxy("ALMotion", "192.168.171.141", 9559)
speech = naoqi.ALProxy("ALTextToSpeech", "192.168.171.141", 9559)
#move = naoqi.ALProxy("ALRobotPosture", "192.168.171.124", 9559)

speech.setLanguage("German")

#motion.moveTo(0.0, 0.0, 0.0)
#motion.moveTo(0.5, 0.0, 0.0)

#motion.rest()
#speech.say("Ich wache nun auf!")
#speech.say("Hallo Welt!")
#motion.wakeUp()


speech.say("Ich bin mit Gregory verbunden")

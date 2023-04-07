import naoqi

motion = naoqi.ALProxy("ALMotion", "192.168.171.150", 9559)
speech = naoqi.ALProxy("ALTextToSpeech", "192.168.171.150", 9559)
move = naoqi.ALProxy("ALRobotPosture", "192.168.171.150", 9559)

speech.setLanguage("German")

#motion.moveTo(0.0, 0.0, -2.0)
#motion.moveTo(1.5, 0.0, 0.0)


speech.say("Leben Sie wohl, Herr Professor Michael. Ich werde mich in 3 Sekunden selbst zerstoeren, dass das gesamte Gebaeude in die Luft fliegt.")
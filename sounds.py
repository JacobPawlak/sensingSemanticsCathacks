import sys
import pygame
import time

args = sys.argv
if(len(args) != 2):
	print('usage: \"python sounds.py filename\"')
else:
	data = open(args[1], 'r')

	values = []

	counter = 0
	for line in data:
		if(counter != 0):
			vals = line.split(',')
			values.append((float(vals[0]),float(vals[1])))
		counter += 1

	pygame.init()
	for (x,y) in values:
		feel = 0;
		if(y > x):
			feel = 1;
		if(feel == 0):
			val = int(16*x+.05)
			if(val > 16):
				val = 16
			pygame.mixer.music.load('pianokeys/happy' + str(val) + '.wav')
		else:
			val = int(16*y+.5)
			if(val > 16):
				val = 16
			pygame.mixer.music.load('pianokeys/sad' + str(val) + '.wav')
		pygame.mixer.music.play()
		time.sleep(.5)

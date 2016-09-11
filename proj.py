#Ryan Shah Jacob Pawlak
#Cathacks II 
#April 9th, 2016
#Go blue team

#SEMANTIC PARSER WITH FILE OUTPUT
from nltk.corpus import sentiwordnet as swn
from nltk import *
import sys
import pygame
import time

def main():
	args = sys.argv
	if(len(args) != 2):
		print('usage: python proj filename')
		return -1
	lines = []
	values = []
	data = open(args[1], 'r')
	for line in data:
		temp = line.split('.')
		for sen in temp:
			tokens = word_tokenize(sen.strip('\n').strip(',').strip('-'))
			if tokens != []:
				lines.append(tokens)
	total_pos = 0
	total_neg = 0

	for line in lines:
		pos = 0.0
		neg = 0.0
		pcount = 0
		ncount = 0
		for word in line:
			sp = 0
			sn = 0
			sub_pos = 0
			sub_neg = 0
			x = swn.senti_synsets(word)
			
			for a in x:
				if(a.pos_score() > 0):
					sub_pos += 1
					sp += a.pos_score()
				if a.neg_score() > 0:
					sub_neg += 1
					sn += a.neg_score()
	#		if(sub_pos != 0):
	#			sp /= sub_pos
	#		if(sub_neg != 0):
	#			sn /= sub_neg
			pos += sp
			neg += sn
			if sp > 0:
				pcount += 1
			if sn > 0:
				ncount += 1
		
		if(pos == 0) or (neg == 0):
			values.append((pos, neg))
			total_pos += pos
			total_neg += neg

		else:	
			values.append((pos/(pos+neg), neg/(pos+neg)))
			total_pos += (pos/(pos+neg))
			total_neg += (neg/(pos+neg))
	print(str(total_pos / len(values)) + ',' + str(total_neg / len(values)))
	for x in range(0, len(lines)):
	#	print('sentence: ' + str(lines[x]))
		print(str(values[x][0]) + ',' + str(values[x][1]))

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

	''' 
	happy = pyglet.media.load('happy.wav')
	sad = pyglet.media.load('sad.wav')
	if(total_pos > total_neg):
		happy.play()
	else:
		sad.play()
	wait(300) '''
main()

#Ryan Shah Jacob Pawlak
#Cathacks II 
#April 9th, 2016
#Go blue team

#SEMANTIC PARSER WITH FILE OUTPUT
from nltk.corpus import sentiwordnet as swn
from nltk import *
import sys

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
			tokens = pos_tag(word_tokenize(sen.strip('\n').strip(',').strip('-')))
			if tokens != []:
				lines.append(tokens)
	total_pos = 0
	total_neg = 0

	for line in lines:
		pos = 0.0
		neg = 0.0
		count = 0
		for word in line:
			tag = 'n'
			if(word[1] == 'VB'):
				tag = 'v'
			if(word[1] == 'JJ'):
				tag = 'a'
			if(word[1] == 'RB'):
				tag = 'r'
			x = swn.senti_synsets(word[0], tag)
			if(x != []):
				for a in x:
					pos += a.pos_score()
					neg += a.neg_score()
				count += 1
		if(pos + neg > 0):
			values.append((pos/(pos + neg), neg/(pos + neg)))
			total_pos += pos
			total_neg += neg
		else:
			values.append((0,0))

	print(str(total_pos / (total_pos + total_neg)) + ',' + str(total_neg / (total_pos + total_neg)))
	for x in range(0, len(lines)):
		print(str(values[x][0]) + ',' + str(values[x][1]))


main()

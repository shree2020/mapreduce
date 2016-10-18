#!/usr/bin/env python

import sys

# input comes from STDIN (standard input)
old_word = "NULL"
min_of_Open = 0
max_of_Open = 0
sum_of_Open = 0
count_of_Open = 0
for line in sys.stdin:
	# remove leading and trailing whitespace
	line = line.strip()
	words = line.split('\t')
	if(old_word == "NULL"):
		old_word = words[0]
		min_of_Open = float(words[1])
		max_of_Open = float(words[1])
		sum_of_Open = float(words[1])
		count_of_Open = float(words[1])+1
		if(float(min_of_Open) > float(words[1])):
			min_of_Open = float(words[1])
		if(float(max_of_Open) < float(words[1])):
			max_of_Open = float(words[1])
		mean_of_Open = float(sum_of_Open)/float(count_of_Open)
		print '\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t' % (words[0],words[1],words[2],words[3],words[4],min_of_Open,max_of_Open,sum_of_Open,count_of_Open,mean_of_Open,words[5])
	elif(old_word==words[0]):
		if(float(min_of_Open) > float(words[1])):
			min_of_Open = float(words[1])
		if(float(max_of_Open) < float(words[1])):
			max_of_Open = float(words[1])
		sum_of_Open = float(sum_of_Open)+float(words[1])
		count_of_Open = float(words[1])+1
		mean_of_Open = float(sum_of_Open)/float(count_of_Open)
		print '\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t' % (words[0],words[1],words[2],words[3],words[4],min_of_Open,max_of_Open,sum_of_Open,count_of_Open,mean_of_Open,words[5])
	else:
		old_word = words[0]
		min_of_Open = float(words[1])
		max_of_Open = float(words[1])
		sum_of_Open = float(words[1])
		count_of_Open = float(words[1])+1
		mean_of_Open = float(sum_of_Open)/float(count_of_Open)
		print '\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t' % (words[0],words[1],words[2],words[3],words[4],min_of_Open,max_of_Open,sum_of_Open,count_of_Open,mean_of_Open,words[5])


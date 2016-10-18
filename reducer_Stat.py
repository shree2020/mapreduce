#!/usr/bin/env python

from operator import itemgetter
import sys
symbol="NULL"
o=0
h=0
l=0
c=0
min_o=0
max_o=0
sum_o=0
n=0
mean_o=0
time="NULL"

# input comes from STDIN (standard input)
for line in sys.stdin:
	# remove leading and trailing whitespace
	line = line.strip()
	words = line.split('\t')
	if(symbol is "NULL"):
		symbol=words[0]
		o=words[1]
		h=words[2]
		l=words[3]
		c=words[4]
		min_o=words[5]
		max_o=words[6]
		sum_o=words[7]
		n=words[8]
		mean_o=words[9]
		time=words[10]
	elif(symbol is words[0]):
		symbol=words[0]
		o=words[1]
		h=words[2]
		l=words[3]
		c=words[4]
		min_o=words[5]
		max_o=words[6]
		sum_o=words[7]
		n=words[8]
		mean_o=words[9]
		time=words[10]
	else:
		sd = ((float(sum_o)-float(mean_o))*(float(sum_o)-float(mean_o)))/float(n)-1
		print '\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t' % (symbol,o,h,l,c,min_o,max_o,sum_o,n,mean_o,sd,time)
		symbol=words[0]
		o=words[1]
		h=words[2]
		l=words[3]
		c=words[4]
		min_o=words[5]
		max_o=words[6]
		sum_o=words[7]
		n=words[8]
		mean_o=words[9]
		time=words[10]
xyz = ((float(words[7])-float(words[9]))*(float(words[7])-float(words[9])))/float(words[8])-1
print '\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t' % (words[0],words[1],words[2],words[3],words[4],words[5],words[6],words[7],words[8],words[9],xyz,words[10])


#!/usr/local/bin/python

'''
Takes a file pointing to a Boroughs-Wheeler Transformed string and a query and returns all the positions of the string in the text.  Returns -1 if string not found.
'''

from sys import argv
from collections import OrderedDict, Counter
from itertools import tee, islice, chain, izip

bwtfile = ""
query = ""
BWTindex = []
originalIndex = []


def previous_and_next(some_iterable):
# utility function for loops
    prevs, items, nexts = tee(some_iterable, 3)
    prevs = chain([None], prevs)
    nexts = chain(islice(nexts, 1, None), [None])
    return izip(prevs, items, nexts)


def getargs():
# Get arguments
	global bwtfile
	global query	
	if len(argv) == 1:
		filename = raw_input("Enter filename:")
		query = raw_input("Enter search string:")
		bwtfile = open(filename).read()
	elif len(argv) != 3:
		print "Expecting 0 or 2 argmuents: <file> <search string>"
	elif len(argv) == 3:
		bwtfile = open(argv[1]).read()
		query = argv[2]

def makeN(file):
# Compute N index
	global N 
	N = OrderedDict()
	Cnt = Counter()
	for char in file:
		Cnt[char] += 1
	K = sorted(dict(Cnt), key=lambda t: t[0])
	for key in K:
		N[key] = Cnt[key]

def makeI(N):
# Compute I index
	global I
	I =  OrderedDict()
	count = 0
	for prev, cur, next in previous_and_next(N.keys()):
		if prev == None:
			I[cur] = 0
		else:
			count += N[prev]
			I[cur] = count 

def makeC(file):
# Compute C-index
	global C
	CCount = Counter()
	C = dict()
	for n, char in enumerate(file):
		C[n] = CCount[char]
		CCount[char] += 1

def RecurSearch(query, place, start, stop, file):
	nums = Counter()
	searchChar = query[place]
	for char in file[start:stop + 1]:
		nums[char] += 1
	if nums[searchChar] == 0:
		return -1
	if place > 0:
		newstart = I[searchChar] + C[start]
		newstop = newstart + N[searchChar] - C[start] - 1
		RecurSearch(query, (place - 1), newstart, newstop, file)		
	else:
		for n in range(start,stop+1):
			if file[n] == searchChar:
				BWTindex.append(n)
		return BWTindex

def RecurTrack(index, file, count):
	if file[index] == '$':
		originalIndex.append(count)
		return
	newindex= I[file[index]] + C[index]
	RecurTrack(newindex, file, count + 1)

def Backtrack(BWTindex, file):
	for index in BWTindex:
		count = -1
		RecurTrack(index, file, count)
	results = sorted(originalIndex)
	print results
	return results
	
def BWTSearch(file, query):
	makeN(bwtfile)
	makeI(N)
	makeC(bwtfile)
	RecurSearch(query, (len(query)-1), 0, (len(file)-1), file)
	Backtrack(BWTindex,file)

getargs()
BWTSearch(bwtfile, query)
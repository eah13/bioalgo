
import random
import matplotlib
import pylab
sequence = open("crYsubset.fa").read()
filtered = ''.join(c for c in sequence if c.isupper())

def random_subsequence(length,string):
	start = random.randint(0,(len(string)-length))
	stop = start + length
	subset = string[start:stop]
	return subset

def getruns(str):
    run=[]
    for i in range(1,len(str)):
        if str[i]==str[i-1]:
            if (i-1) not in run:
                run.append(i-1)
            run.append(i)
    return len(run)

def BWT(s): 
    rotation = [s[i:] + s[:i] for i in xrange(len(s))] 
    rotation.sort() 
    return "".join([r[-1] for r in rotation])

def plot(string,times,length):
	x = []
	y = []
	for n in range(times):
		subseq = random_subsequence(length,string)
		BWTseq = BWT(subseq)
		if len(subseq) != length:
			print "Warning: short subseq"
		if len(BWTseq) != length:
			print "Warning: short subseq"
		regruns = getruns(subseq)
		bwtruns = getruns(BWTseq)
		if regruns > 200:
			print regruns, " ", bwtruns
		x.append(regruns)
		y.append(bwtruns)	
	matplotlib.pyplot.scatter(x,y)
	matplotlib.pyplot.axis([0,100,0,100])
	matplotlib.pyplot.show()

plot(filtered,500,100)

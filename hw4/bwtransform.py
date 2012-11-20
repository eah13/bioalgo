
from sys import argv


def BWT(s, f):
		
		rotation = [s[i:] + s[:i] for i in xrange(len(s))] 
		# sort rows alphabetically
		rotation.sort() 
		# return (last column of the table)
		bwt = "".join([r[-1] for r in rotation])
		output = open(f, 'w')
		output.write(bwt)

def getargs():
	global string
	global file
	if len(argv) == 3:
		string = argv[1]
		file = argv[2]
	
	elif len(argv) ==1:
				
		print "This is a script to perform Burrows-Wheeler Transformations on strings."
		print "Be sure to include an end-of-string character ('$') at the end."
		string = raw_input("Enter string:")
		file = raw_input("Enter filename:")
	
	else:
		print "Usage: <string> <file>"
		return -1

string = ""
file = ""
getargs()
BWT(string, file)
#!usr/bin/python

def printTableu(tableu):
 print "input graph:"
 print '-'*20
 for row in tableu:
  print row
 print '-'*20
 return
  
G = [  [],
   [2,6,8,9],
   [1,3,4,8],
   [2,4],
   [2,3],
   [7,8],
   [1,9],
   [5,8],
   [1,2,5,7],
   [1,6]]

E =[ [1,2],
	[2,3],
	[3,1],
	[1,4],
	[4,1]]

printTableu(E)


def Euler (E, location):
 stack = []
 path = []
 while (len(stack) > 0) or (len(E[location]) > 0):
  if (len(E[location]) > 0):
   stack.append(location)
   location = E[location].pop(0)
  elif (len(stack) > 0):
   path.append(location)
   location = stack.pop()
 path.append(location)
 return path


circuit = Euler(E, 1)
print circuit

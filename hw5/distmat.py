A = [0,18,15,21,6,16]
B = [18,0,23,19,20,24]
C = [15,23,0,26,17,19]
D = [21,19,26,0,23,27]
E = [6,20,17,23,0,18]
F = [16,24,19,27,18,0]



matrix = [A,B,C,D,E,F]


def find_triples():
	

	matches = []
	triples = 0

	for i in xrange(0,5):
		for j in xrange(0,5):
			for k in xrange(0,5):
				
				if matrix[i][j] == 0:
					break
				elif matrix[j][k] == 0:
					break
				elif matrix[i][k] == 0:
					break
				elif (matrix[i][j] + matrix[j][k]) >= matrix[i][k]:
					# print matrix[i][j]," + ",matrix[j][k]," > ",matrix[i][k]
					matches.append([i,j,k])	
					triples += 1

	m = sorted(matches)
	for match in m:
	 	print matrix[match[0]][match[1]], matrix[match[1]][match[2]], matrix[match[0]][match[2]]


find_triples()

def four_point():
# Determines whether a matrix is additive by testing for the four point condidtion.  Expects matrix as a list of lists

	n = len(matrix)

	for i in xrange(0,n):
		for j in xrange(0,n):
			if i == j:
				continue
			for k in xrange(0,n):
				if k == j:
					continue
				if k == i:
					continue
				for l in xrange(0,n):
					if l == k:
						continue
					if l == j:
						continue
					if l == i:
						continue
					one = matrix[i][j] + matrix[k][l]
					two = matrix[i][k] + matrix[j][l]
					three = matrix[i][l] + matrix[j][k]
					lump = sorted([one,two,three])
					if lump[1] != lump[2]:
						print "Not additive"


def sankoff():

	chimp = ['G','T','T','G']
	gorilla = ['G','T','C','A']
	human = ['A','C','C','A']
	orangutan = ['A','T','T','A']

	A = [0,2,3,8]
	T = [2,0,1,3]
	C = [3,1,0,3]
	G = [8,3,3,0]

	matrix = [A,T,C,G]






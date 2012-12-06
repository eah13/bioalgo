
A = [0,18,15,21,6,16]
B = [18,0,20,19,20,24]
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

	matches.sort()
	for match in matches:
	 	print matrix[match[0]][match[1]], matrix[match[1]][match[2]], matrix[match[0]][match[2]]

	if len(matches) == triples:
		print "All triples satisfy d(i,j) + d(j,k) >= d(i,k)"
	else:
		print "Not additive"

def four_point():

	mismatch = []

	for i in xrange(0,5):
		for j in xrange(0,5):
			if i == j:
				continue
			for k in xrange(0,5):
				if k == j:
					continue
				if k == i:
					continue
				for l in xrange(0,5):
					if l == k:
						continue
					if l == j:
						continue
					if l == i:
						continue
					one = matrix[i][j] + matrix[k][l]
					two = matrix[i][k] + matrix[j][l]
					three = matrix[i][l] + matrix[j][k]
					lump = [one,two,three]
					together = set(lump)
					if len(together) != 2:
						print i,j,k,l
						print lump
						print matrix[i][j]," + ",matrix[k][l]," = ",one
						print matrix[i][k]," + ",matrix[j][l]," = ",two
						print matrix[i][l]," + ",matrix[j][k]," = ",three
						print together


four_point()

!#/bin/usr/python

# Analyze the codon biases of the human genome

# Read in data on codons
# count = { codons | AA | n = 0 }

# Read in 4 mRNA-offset pairs from CL offsets

# For each input mRNA:
# 	From the offset, read every three characters
#		if the chars = STOP
#			break & next sequence
#		else look up codon and increment corresponding count

# Pseudocode
# 1 = 0
# For j in sequences
#	for i in sequence
#		\\ while condition stop codon or i condition
#		print <proteinjname> ?
#		<proteinj> = { sequence name & AAs }
#		codon = { i, i +1, i +2}
#		i = i +3
#		if codon is in {codons} 
#			count ++
#			append {codon:AA} to <proteinname>
#		else i++
#	print <proteinj>
#	j++
# For AA in Count
#	sum = { n1, n2 , n3 }
#	print AA, codon, div(n1, sum) x3

# Output should be:
# amino acids & codons & relative frequencies

OK.
Table:
Ammino acids, codons, and counts

Store seqeunce as list
Store start index
go to index in list

for i to 3
append current_codon with list_i

when current_codon = codon in table
count +1

do until all arguments are read

print table



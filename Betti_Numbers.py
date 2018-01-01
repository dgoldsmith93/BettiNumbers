import numpy as np
from numpy.linalg import matrix_rank

def TDA(ASC):

	# Read in raw Abstract Simplicial Complex (ASC) as string.
	A = ASC.split()

	# convert ASC from string into list of lists of p-chains.
	m = len(max(A, key = len))

	L = [[] for val in range(0, m)]
	
	
	for val in range(0, len(A)):
		length = len(A[val])
		L[m - (length)].append(''.join(sorted(A[val]))) # want to make p-chains abelian
		
	print "\n", "Abelian Simplicial Complex = ", L, "\n"


#	v = ['bac']

#	if(L[0][0] == v[0]):	
#		print 'great'
#	else:
#		print 'nooooo'
#	w = ''.join(sorted(L[0][0]))
#	print w

	
#	for a in range(0,len(L)):
#		for b in range(0,len(L[a]))
#			L[a][b] = sorted(L[a][b])
#		print "new L = ", L


	boundary = [[] for val in range(0, m)]
	
	# create boundary operator results
	for i in range(0, len(L)):
		for j in range(0,len(L[i])):
			delta = []
			for k in range(0,len(L[i][j])):
				Q = L[i][j].replace(L[i][j][k], "")
				delta.append(Q) #makes boundary abelian				
			boundary[i].append(delta)
	print "Boundary = ", boundary, "\n"
	#print sorted(boundary[1])

	# create boundary matrices of: p-1 by p
	matrices = []
	#print "boundary[1]", boundary[1]
	for i in range(0,len(L) - 1): #can't have a -1 simplex
		z = np.zeros((len(L[i+1]),len(L[i])))
		#print "i = ", i
		for k in range(0,len(L[i])):
			#print "k = ", k

			for j in range(0,len(L[i+1])): #iterating over p-1 simplices
				#print "j = ", j
			#print "max k = ", len(boundary[i][j])
			
			#for k in range(0,len(boundary[i][j])):				
			#	print "k = ", k
				#print "L[i +1][j] = ", L[i +1][j]
			
				#print "sorted(boundary[i][k]) = ", (sorted(boundary[i][k]))
				if(L[i +1][j] in sorted(boundary[i][k])):
					#== ''.join(sorted(boundary[i][j][k]))):
					#print "index = ", sorted(boundary[i][k]), (L[i +1][j])
					z[j,k] = 1 #Think the issue is here, where j does not change to keep up with k
			#print "z = \n", z
		matrices.append(z)
	print "Raw Matrices = \n", matrices, "\n"
	#print L[0], L[1], z

	# Smith Normal Form
	def row_add(z, current, adding):
		z[current,:] = np.add(z[current,:], z[adding,:]) % 2
	def col_add(z, current, adding):
		z[:, current] = np.add(z[:, current], z[:, adding]) % 2

	raw_matrices = matrices[:]

	for q in range(0,len(matrices)):
		m, n = matrices[q].shape
		ind = min(m,n)
		#print "ind = ", ind
		for p in range(0,ind):
			if matrices[q][p,p] != 1:
				for i in range(p+1,m):					
					if matrices[q][i,p] == 1:
						row_add(matrices[q],p,i)
						break
			if matrices[q][p,p] != 1:
				for i in range(p+1,n):					
					if matrices[q][p, i] == 1:
						col_add(matrices[q],p,i)
						break

			for j in range(p+1,m):
				if  matrices[q][j,p] == 1:
					row_add(matrices[q], j, p)
					#print matrices[q]	
			for k in range(p+1,n):
				if matrices[q][p,k] == 1:
					col_add(matrices[q], k, p)
					#print matrices[q]
	print "Smith Normal Forms \n", matrices

#find betti numbers
#zero columns are Z and rank is B. Betti Numbers: H = Z - B
	#Z0 = len((matrices[len(matrices)-1]))-1
	Z0 = len(L[len(L)-1]) - 1
	#print "akjbfkjabdf", L[len(L)-1]
	Z = []
	B = [0]
	Betti = []
	
	#print "Z0 = ", Z0
	for i in range(0, len(matrices)):		
		Z.append(len(matrices[i][0]) - matrix_rank(matrices[i]))
		B.append(matrix_rank(matrices[i]))
		#print "length of matrix", i,"is", len(matrices[i]), "Z = ", Z[i+1], "B = ", B[i]
	Z.append(Z0)
	
	for i in range(0,len(Z)):
		Betti.append(Z[i] - B[i])
	print "Z = ", Z, " ", "B = ", B, "\n" "Betti = ", Betti

def main():
	Complex = input("Enter Abstract Simplicial Complex: ")
	TDA(Complex) 

main()
# 'ab bc ac a b c ad dc d'
# 'abc adc ab bc ac a b c ad dc d'
# 'abc adc bdc abd ab bc ac bd a b c ad dc d'
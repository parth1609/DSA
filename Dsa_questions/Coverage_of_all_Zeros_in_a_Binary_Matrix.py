# Coverage of all Zeros in a Binary Matrix



class Solution:
	def findCoverage(self, matrix):
		# Code here
		n = len(matrix)
		m = len(matrix[0])
		coverage = 0
		for i in range(n):
		    for j in range(m):
		        if matrix[i][j] == 0:
		            
		            if i > 0 and matrix[i-1][j] == 1: # up
		                coverage +=1
		            if i < n-1 and matrix[i+1][j] == 1: # Down
		                coverage+=1
		            if j < m-1 and matrix[i][j+1] == 1: # right
		                coverage+=1
		            if j > 0 and matrix[i][j-1] == 1: #left 
		                coverage+=1
      return coverage

#User function Template for python3
class Solution:
	def matSearch(self, mat, x):
		# Complete this function
        row = len(mat)
        col = len(mat[0])
        i = 0
        j = col-1
        while i<row and j>=0:
            if mat[i][j] == x:
                return True
            elif mat[i][j] > x:
                j-=1
            else:
                i+=1
        return False

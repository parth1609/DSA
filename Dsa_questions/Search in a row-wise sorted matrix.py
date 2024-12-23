
class Solution:
    def findx(self,arr,x):
        i = 0
        j = len(arr) -1
        while i<=j:
            mid = (i+j)//2
            if arr[mid] == x:
                return True
            elif arr[mid] < x:
                i = mid+1
            else:
                j = mid-1
        return False
    
    #Function to search a given number in row-column sorted matrix.
    def searchRowMatrix(self, mat, x): 
    	for row in mat:
    	    if self.findx(row,x):
    	        return True
    	return False
    	

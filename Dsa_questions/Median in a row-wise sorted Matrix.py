
class Solution:
    def findlow(self,mat,n):
        min_ = mat[0][0]
        for i in range(1,n):
            if mat[i][0] < min_:
                min_ = mat[i][0]
        return min_
    
    def findhigh(self,mat,n,m):
        max_ = mat[0][m-1]
        for i in range(1,n):
            if mat[i][m-1] > max_:
                max_ = mat[i][m-1]
        return max_
    
    def upper_bound(self,arr,elem):
        low = 0
        high = len(arr) - 1
        ans = len(arr)
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] > elem:
                ans  = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans
            
    
    def find_smaller_elements(self,mat,n,m,mid):
        count = 0
        for i in range(n):
            count += self.upper_bound(mat[i],mid)
        return count
            
    def median(self, mat):
    	n = len(mat) # length of rows
    	m = len(mat[0]) # length of columns
    	
    	low = self.findlow(mat,n)
    	high = self.findhigh(mat,n,m)
    	
    	while low <= high:
    	    mid = (low + high) // 2
    	    required_elements = (n*m)//2
    	    smaller_elements = self.find_smaller_elements(mat,n,m,mid)
    	    if smaller_elements <= required_elements:
    	        low = mid + 1
    	    else:
    	        high = mid - 1
    	        

        return low

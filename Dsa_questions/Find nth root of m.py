#User function Template for python3
class Solution:

    def find_mid(self , mid, n, m):
        for i in range(n):
            ans  = mid ** n
            if ans > m:
                return 2
            if ans == m:
                return 1
            return 0
        
	def nthRoot(self, n: int, m: int) -> int:
		# Code here
		if n == 1:  
            return m
        if m == 0:  
            return 0
                        
		    
	    low, high = 1, m  
        while low <= high:
            mid = (low + high) // 2
            midn = self.find_mid(mid, n, m)
            if midn == 1: 
                return mid
            elif midn == 2:  
                high = mid - 1
            else: 
                low = mid + 1
	    return -1
        

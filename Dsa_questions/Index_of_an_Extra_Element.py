class Solution:
    def findExtra(self,n,a,b):
        #add code here
        left  = 0
        right = n-1
        
        while left<right:
            mid = (left + right)//2
        
            if a[mid] == b[mid]:
                left  = mid+1
            else:
                right = mid
        return left 
                

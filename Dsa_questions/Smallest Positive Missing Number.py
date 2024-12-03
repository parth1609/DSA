class Solution:
    
    #Function to find the smallest positive number missing from the array.
    def missingNumber(self,arr):
        #Your code here
        n = len(arr)
        res = [0]*n
        for i in range(n):
            if 0 < arr[i] <= n:
                res[arr[i] - 1] = 1
                
        for i in range(n):
            if res[i] == 0:
                return i+1
        return n+1
        

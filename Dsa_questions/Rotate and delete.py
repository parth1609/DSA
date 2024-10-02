
class Solution:
    def rotateDelete(self,  arr):
        # code here
        n = len(arr)
        m = n//2
        for k in range(1,m+1):
            arr = [arr[-1]] + arr[:-1]
            i = len(arr)-k
            arr.pop(i)
        
        return arr[0]
        
        
        

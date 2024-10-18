
class Solution:
    
    def getSingle(self,arr):
        # code here
        op = arr[0]
        for i in range(1,len(arr)):
            op ^= arr[i]
        
        return op

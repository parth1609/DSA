class Solution:
    def pairWithMaxSum(self, arr):
        #code here
        if len(arr) < 2:
            return -1
        result  = arr[0] + arr[1]
        for i in range(1,len(arr)-1):
            result  = max(result, arr[i] + arr[i+1])
        
        return result 

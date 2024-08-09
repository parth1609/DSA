
class Solution:
    def Maximize(self, arr): 
        # Complete the function
        m = 1000000007
        arr.sort()
        maxsum = 0
        for i in range(len(arr)):
            maxsum += arr[i] * i
        
        return maxsum%m
      

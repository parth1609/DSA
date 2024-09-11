#User function Template for python3

class Solution:
    def lenOfLongSubarr (self, arr, n, k) : 
        #Complete the function
        length = 0
        PreSumMap = {}
        s = 0
        for i in range(n):
            s+=arr[i]
            if s==k:
                length = max(length, i+1)
            
            remaining_sum = s - k
            
            if remaining_sum in PreSumMap:
                size = i - PreSumMap[remaining_sum]
                length  = max(length, size)
            
            if s not in PreSumMap:
                PreSumMap[s] = i
                    
        return length 

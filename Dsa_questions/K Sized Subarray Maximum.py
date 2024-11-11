from collections import deque
class Solution:
    #Function to find maximum of each subarray of size k.
    def maxOfSubarrays(self, arr, k):
        n = len(arr)
        qu = deque()
        ans = []
        for i in range(n):
            while qu and arr[qu[-1]] < arr[i]:
                qu.pop()
            
            qu.append(i)
            
            if qu[0] < i - k + 1:
                qu.popleft()
            
            if i >= k-1:
                ans.append(arr[qu[0]])
        
        return ans
            

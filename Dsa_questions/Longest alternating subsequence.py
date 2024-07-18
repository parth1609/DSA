class Solution:
    # Function to find the maximum length of alternating subsequence
    def alternatingMaxLength(self, arr):
       #code here
       low = 1
       high = 1
       for i in range(1,len(arr)):
           if arr[i] > arr[i-1]:
               low = high +1
           if arr[i] < arr[i-1]:
               high = low +1
       return max(low,high)

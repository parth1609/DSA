class Solution:
    def findKRotation(self, arr):
        # code here
        n = len(arr)
        if arr[0] > arr[n-1]:
            for i in range(n):
                if arr[i] > arr[i+1]:
                    return i+1
        return 0

class Solution:
    def rearrange(self, arr):
        #Code here
        n = len(arr)
        i=0
        while i<n:
            if arr[i] >= 0 and arr[i] != i:
                arr[arr[i]], arr[i] = arr[i], arr[arr[i]]
            else:
                i+=1
        return arr

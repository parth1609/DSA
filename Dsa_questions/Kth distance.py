class Solution:
    def checkDuplicatesWithinK(self, arr, k):
        # your code
        duplicate = []
        for i in range(len(arr)):
            if arr[i] in duplicate:
                return True
            
            duplicate.append(arr[i])
            
            if i>=k:
                duplicate.remove(arr[i-k])
        return False
        
        

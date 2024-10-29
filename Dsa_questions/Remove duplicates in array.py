class Solution:
    def removeDuplicates(self, arr):
        # code here 
        li = {}
        for i in range(len(arr)):
            if arr[i] not in li:
                li[arr[i]] = 1
            else:
                li[arr[i]] += 1
        
        return li.keys()


class Solution:
    def longestCommonPrefix(self, arr):
        # code here
        if not arr:
            return -1
        arr.sort()
        flag = True 
        prefix = ""
        for i in range(len(arr[0])):
            p = arr[0][i]
            for j in range(1,len(arr)):
                if arr[j][i] == p:
                    flag = True 
                else:
                    flag = False
                    
            if flag == True:
                prefix += p
            else:
                break 
            
        return prefix if len(prefix)!= 0 else -1

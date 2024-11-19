class Solution:
    def getSecondLargest(self, arr):
        # Code Here
        s_largest  = largest = 0
        for num in arr:
            if num > largest:
                s_largest = largest 
                largest = num
            elif largest > num and num > s_largest:
                s_largest  = num
        if s_largest == 0:
            return -1
        return s_largest 
                


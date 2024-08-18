class Solution:
    def canSplit(self, arr):
        #code here
        total_sum = sum(arr)
        left_sum = 0
        for num in arr:
            total_sum -= num
            left_sum += num
            if total_sum == left_sum:
                return True
        return False 
            

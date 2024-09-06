class Solution:
   
    def maxSubArraySum(self,arr):
        ##Your code here
        max_sum = arr[0]
        summ = 0
        for i in range(len(arr)):
            summ += arr[i]
            
            max_sum = max(summ,max_sum)
            
            if summ < 0:
                summ = 0
            
        return max_sum

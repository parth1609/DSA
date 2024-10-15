
class Solution:
    
    #Complete this fuction
    #Function to count the number of subarrays which adds to the given sum.
    def subArraySum(self,arr, tar):
        #Your code here
        total = 0
        count = 0
        mapp = {0:1}
        for num in arr:
            total += num
            if total - tar in mapp:
                count += mapp[total-tar]
                
            if total in mapp:
                mapp[total] += 1
            else:
                mapp[total] = 1
        
        return count 

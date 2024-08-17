class Solution:
    def productExceptSelf(self, nums):
        #code here
        n = len(nums)
        left = [0]*n
        right = [0]*n
        productlist = [0]*n
        
        left[0] = 1
        right[n-1] = 1
        
        for i in range(1,n):
            left[i] = nums[i-1]  * left[i-1]
        
        for j in range(n-2,-1,-1):
            right[j] = nums[j+1] * right[j+1]
        
        for i in range(n):
            productlist[i] = left[i] * right[i]
        
        return productlist

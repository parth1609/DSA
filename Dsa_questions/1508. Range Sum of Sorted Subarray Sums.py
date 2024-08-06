class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        m = 1000000007
        count = []
       
        for i in range(len(nums)):
            mxsm = 0 
            for j in range(i,len(nums)):
                mxsm += nums[j]
                count.append(mxsm)
        
        count.sort()
        return sum(count[left-1:right])%m
            
                

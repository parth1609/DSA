# 1509. Minimum Difference Between Largest and Smallest Value in Three Moves

class Solution:
    def minDifference(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        if n <= 4:
            return 0
        result  = float('inf')
        result  = min(result,nums[n-4] - nums[0])
        result  = min(result,nums[n-1] - nums[3])
        result  = min(result,nums[n-3] - nums[1])
        result  = min(result,nums[n-2] - nums[2])

        return result 
        

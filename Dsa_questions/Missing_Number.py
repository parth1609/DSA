# 268. Missing Number

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # O(n) Time
        n = len(nums)
        n_natural_sum = (n * (n+1))//2
        nums_sum = sum(nums)
        return n_natural_sum   - nums_sum
        

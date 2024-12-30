import math
class Solution:
    def below_threshhold(self,nums,divisor,threshold):
        total = 0
        for num in nums:
            total += math.ceil(num/divisor)
        return True if total <= threshold else False

    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left = 1
        right = max(nums)
        while left <= right:
            mid = (left + right) // 2
            if self.below_threshhold(nums,mid,threshold):
                right = mid - 1
            else:
                left = mid + 1
        return left
        

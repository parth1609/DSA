# 35. Search Insert Position

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        while left <= right:
            mi = (left  + right)//2
            if nums[mi] == target:
                return mi
            elif nums[mi] < target:
                left = mi + 1
            else:
                right = mi - 1
        return left 
            
            

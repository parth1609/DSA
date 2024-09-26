class Solution:
    def findMin(self, nums: List[int]) -> int:
        length = len(nums)
        left = 0
        right = length-1
        while left < right:
            mi = (left+right)//2
            if nums[mi] > nums[right]:
                left  = mi + 1
            else:
                right = mi
        
        return nums[left]

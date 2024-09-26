class Solution:
    def findMin(self, nums: List[int]) -> int:
        left  = 0
        right  = len(nums)-1
        while left <= right:
            mi = (left+right)//2
            if nums[mi] > nums[right]:
                left = mi + 1
            elif nums[mi] < nums[right]:
                right = mi
            else:
                right -= 1
        
        return nums[left]

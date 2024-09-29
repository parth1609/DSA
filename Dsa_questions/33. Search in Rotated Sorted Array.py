class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        while left <= right:
            mi = (left+right)//2
            if nums[mi] == target:
                return mi
            
            if nums[left] <= nums[mi]:
                if nums[left] <= target < nums[mi]:
                    right = mi - 1
                else:
                    left = mi + 1
            else:
                if nums[mi] < target <= nums[right]:
                    left = mi + 1
                else:
                    right = mi -1
        return -1
                     

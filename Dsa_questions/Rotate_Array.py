#189. Rotate Array

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        a = k % len(nums)
        nums[:] = nums[-a:] + nums[:-a]
        return nums

        
        

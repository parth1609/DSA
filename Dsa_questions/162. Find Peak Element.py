class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        if nums[0] > nums[1]:
            return 0
        if nums[n-1] > nums[n-2]:
            return n-1
        
        low = 1
        high  = n-2
        while low<=high:
            mi = (low + high) // 2
            if nums[mi-1] < nums[mi]  > nums[mi+1]:
                return mi
            if nums[mi] < nums[mi+1]:
                low = mi + 1
            else:
                high = mi - 1
        return -1

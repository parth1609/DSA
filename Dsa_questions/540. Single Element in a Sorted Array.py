class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        if nums[0] != nums[1]:
            return nums[0]
        if nums[n-1] != nums[n-2]:
            return nums[n-1]
        low = 1
        high = n-2
        while low <= high:
            mi = (low + high) // 2
            if nums[mi] != nums[mi-1] and nums[mi] != nums[mi+1]:
                return nums[mi]
            # To avoid to find in left half
            if (mi % 2 == 1 and nums[mi] == nums[mi-1]) or (mi % 2 == 0 and nums[mi] == nums[mi+1]):
                low = mi + 1
            else:
                high = mi - 1
        return -1

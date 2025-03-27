class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        n = len(nums)
        low = 0
        high = n-1
        while low <= high:
            mid = (low + high)//2
            if nums[mid] > 0:
                high = mid - 1
            else:
                low = mid + 1
        positive = n-low 

        low = 0
        high = n-1
        while low <= high:
            mid = (low+high)//2
            if nums[mid] < 0:
                low = mid + 1
            else:
                high = mid - 1
        negative = high + 1

        return max(positive, negative)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in nums and i != nums.index(diff):
                return [i, nums.index(diff)]
            

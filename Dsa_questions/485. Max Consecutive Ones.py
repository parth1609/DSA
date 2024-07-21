class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxons = 0
        current_one = 0
        for i in nums:
            if i == 1:
                current_one+=1
            else:
                current_one = 0
            maxons = max(maxons,current_one)
        return maxons

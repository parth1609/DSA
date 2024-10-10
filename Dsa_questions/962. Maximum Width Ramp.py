class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        stack  = []
        n = len(nums)
        max_ = 0
        for i in range(n):
            if not stack or nums[i] <= nums[stack[-1]]:
                stack.append(i)
        for j in range(n-1,-1,-1): 
            while stack and nums[j] >= nums[stack[-1]]:
                max_ = max(max_, j-stack.pop())
            
        return max_

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        element = None 

        for i in range(len(nums)):
            if count ==0:
                count = 1
                element = nums[i]
            elif element == nums[i]:
                count += 1
            else:
                count -= 1
        
        kount = 0
        for i in range(len(nums)):
            if element == nums[i]:
                kount +=1
        if kount > len(nums)//2:
            return element
        return -1

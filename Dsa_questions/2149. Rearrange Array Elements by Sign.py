class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        new_array = [0] * n
        pos = 0
        neg = 1
        for num in nums:
            if num > 0:
                new_array[pos] = num
                pos+=2
            else:
                new_array[neg] = num
                neg += 2
        
        return new_array

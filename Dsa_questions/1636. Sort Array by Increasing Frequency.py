class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        hash_map = {nums[i]:nums.count(nums[i]) for i in range(len(nums))}
        nums.sort(key= lambda x:(hash_map[x],-x) )
        return nums

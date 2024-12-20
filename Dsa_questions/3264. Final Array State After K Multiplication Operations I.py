from heapq import heapify, heappop, heappush
class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        min_heap = [(val,i) for i,val in enumerate(nums)]
        heapify(min_heap)
        
        for _ in range(k):
            _,i= heappop(min_heap)
            nums[i] *= multiplier
            heappush(min_heap, (nums[i],i))
        
        return nums

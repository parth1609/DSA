import math
class Solution:
    def count_hrs(self,arr,mid, h):
        total = 0
        for num in arr:
            total += math.ceil(num / mid)
        return total 

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        high = max(piles)
        low = 1
        while low <= high:
            mid = (low + high) // 2
            total_hrs = self.count_hrs(piles,mid,h)
            if total_hrs <= h :
                high = mid - 1
            else:
                low = mid + 1
        return low
             
        

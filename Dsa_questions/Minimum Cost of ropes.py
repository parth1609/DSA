from heapq import heapify, heappush,heappop
class Solution:
    def minCost(self, arr) -> int:
        min_heap = []
        total_cost = 0
        heapify(min_heap)
        for rope in arr:
            heappush(min_heap,rope)
        while len(min_heap) >= 2:
            first = heappop(min_heap)
            second = heappop(min_heap)
            new_rope = first + second
            total_cost += new_rope
            heappush(min_heap,new_rope)
        
        return total_cost

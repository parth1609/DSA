from heapq import heapify,heappop
class Solution:
    def replaceWithRank(self, N, arr):
        # by default it is a min_heap in python
        min_heap = list(set(arr))   
        heapify(min_heap)
        
        rank_map = {}
        rank = 0
        
        while min_heap:
            num = heappop(min_heap)
            rank += 1
            rank_map[num] = rank
        result = [rank_map[num] for num in arr]
        return result

from heapq import heappush, heappop, heapify
class Solution:
    def printKClosest(self, arr, n, k, x):
        max_heap = []
        heapify(max_heap)
        ans = []
        for num in arr:
            if num == x:
                continue
            heappush(max_heap, (-abs(num - x),num))
            if len(max_heap) > k:
                heappop(max_heap)
        while max_heap:
            diff,num = heappop(max_heap)
            ans.append(num)
        return ans[::-1]
        

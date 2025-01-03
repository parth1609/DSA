from heapq import heapify,heappush, heappop
class Solution:

    def kthSmallest(self, arr,k):
        max_heap = []
        heapify(max_heap)
        for num in arr:
            heappush(max_heap,-num)
            if  len(max_heap) > k:
                heappop(max_heap)
                
        return -max_heap[0]
                
        

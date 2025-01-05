from heapq import heapify, heappush, heappop
class Solution:
    def nearlySorted(self, arr, k):
        min_heap = []
        i = 0
        for num in arr:
            heappush(min_heap,num)
            if len(min_heap) > k:
                arr[i] = heappop(min_heap)
                i+=1
        while min_heap:
            arr[i] = heappop(min_heap)
            i+=1
        return arr

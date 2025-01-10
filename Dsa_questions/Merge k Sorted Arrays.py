from heapq import heapify,heappop,heappush
class Solution:
    #Function to merge k sorted arrays.
    def mergeKArrays(self, arr, K):
        result = []
        min_heap = []
        heapify(min_heap)
        for i in range(len(arr)):
            for j in range(len(arr)):
                heappush(min_heap,arr[i][j])
        while min_heap:
            result.append(heappop(min_heap))
            
        return result
            
        

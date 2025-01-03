from heapq import heappop, heappush, heapify
class Solution:

	def kLargest(self,arr, k):
		# code here
		min_heap = []
		heapify(min_heap)
		for num in arr:
		    heappush(min_heap,num)
		    if len(min_heap) > k:
		        heappop(min_heap)
		return sorted(min_heap, reverse=True)
                        

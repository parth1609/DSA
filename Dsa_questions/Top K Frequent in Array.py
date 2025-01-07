from heapq import heapify, heappush,heappop
class Solution:
	def topKFrequent(self, arr, k):
		min_heap =[]
		freq = {}
		ans  = []
		
		for num in arr:
		    if num not in freq:
		        freq[num] = 1
		    else:
		        freq[num] += 1
		heapify(min_heap)
		for key, value in freq.items():
		    heappush(min_heap, (value,key))
		    if len(min_heap) > k:
		        heappop(min_heap)
		
		while min_heap:
		    value,key = heappop(min_heap)
		    ans.append(key)
		    
		return ans[::-1]

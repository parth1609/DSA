from heapq import heapify, heappush,heappop
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []
        result = []
        for point in points:
            sq = point[0]*point[0] + point[1]*point[1]
            heappush(max_heap,(-sq,(point[0],point[1])))
            if len(max_heap) > k:
                heappop(max_heap)
        while max_heap:
            distance,point = heappop(max_heap)
            result.append(point)
        return result[::-1]

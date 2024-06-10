# Height Checker
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sort_array = sorted(heights)
        count  = 0
        for i in range(len(heights)):
            if heights[i] != sort_array[i]:
                count += 1
        return count 

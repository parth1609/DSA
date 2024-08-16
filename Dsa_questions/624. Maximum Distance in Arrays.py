class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        current_minimum = arrays[0][0]
        current_maximum = arrays[0][-1]
        result = 0
        for i in range(1, len(arrays)):
            array = arrays[i]
            result = max(result, abs(array[-1] - current_minimum), abs(current_maximum - array[0]))
            current_minimum = min(current_minimum, array[0])
            current_maximum = max(current_maximum, array[-1])

        return result

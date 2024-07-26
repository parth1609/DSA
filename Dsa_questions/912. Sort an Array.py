from collections import Counter
from typing import List
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        output = []
        for num in sorted(count.keys()):
            output += [num] *  count[num]
        return output

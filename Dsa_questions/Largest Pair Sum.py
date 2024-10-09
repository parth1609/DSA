from typing import List


class Solution:
    def pairsum(self, arr : List[int]) -> int:
        # code here
        if len(arr) < 2:
            return 0
            
        if arr[0] > arr[1]:
            first = arr[0]
            second = arr[1]
        else:
            first = arr[1]
            second = arr[0]
        
        for i in range(2,len(arr)):
            if arr[i] > first:
                second = first 
                first = arr[i]
            elif arr[i] > second:
                second = arr[i]
        
        return first + second

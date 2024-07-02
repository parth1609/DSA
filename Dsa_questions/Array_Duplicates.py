# Array Duplicates


from typing import List


class Solution:
    def duplicates(self, n : int, arr : List[int]) -> List[int]:
        # code here
        li = {}
        for i,num in enumerate(arr):
            if num in li:
                li[num] +=1
            else:
                li[num] =1
        result = []
        for key,value in li.items():
            if key > 1:
                result.append(key)
            else:
                return [-1]
        return result 
        

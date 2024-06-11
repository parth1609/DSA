#Relative Sort Array

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        out = {}
        # record the count of each element in arr1
        for num in arr1:
            if num in out:
                out[num] +=1
            else:
                out[num] = 1
        
        
        result  = []
        for num in arr2:
            # return element of out[num] of times 
            result.extend([num] * out[num])
          
        # for remaining element which is not present in arr2
        remaining = [num for num in arr1 if num not in arr2]
        result.extend(sorted(remaining))

        return result 

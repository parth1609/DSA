from typing import List


class Solution:
    def zigZag(self, n : int, arr : List[int]) -> None:
        # code here
        flag = True 
        for i in range(n-1):
            if flag == True:
                if arr[i] > arr[i+1]:
                    arr[i], arr[i+1] = arr[i+1], arr[i]
            else:
                if arr[i] < arr[i+1]:
                    arr[i], arr[i+1] = arr[i+1], arr[i]
                    
            flag = bool(1-flag)
        
        return arr
        

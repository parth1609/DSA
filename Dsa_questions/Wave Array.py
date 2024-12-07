from typing import List


class Solution:
    def convertToWave(self, arr : List[int]) -> None:
        # code here
        n = len(arr)
        for i in range(0,n,2):
            if (i>0 and arr[i] < arr[i-1]):
                arr[i], arr[i-1] = arr[i-1], arr[i]
            if (i<n-1 and arr[i] < arr[i+1]):
                arr[i], arr[i+1] = arr[i+1],arr[i]
        
        


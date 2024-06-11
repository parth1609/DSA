# Maximum Tip Calculator


from typing import List


class Solution:
    def maxTip(self, n : int, x : int, y : int, arr : List[int], brr : List[int]) -> int:
        
        orders = [(arr[i], brr[i], abs(arr[i] - brr[i]),i) for i in range(n)]
        orders.sort(key=lambda x:x[2], reverse = True)
        
        total_tip = 0
        countA = 0
        countB = 0
        
        for tip in orders:
            if (tip[0] > tip[1] and countA <x) or countB >= y:
                total_tip += tip[0]
                countA +=1
            else:
                total_tip += tip[1]
                countB +=1
        
        return total_tip
       

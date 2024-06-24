# Summed Matrix


class Solution:
    def sumMatrix(self, n, q):
        # code here 
        if q < 1 or q > 2*n:
            return 0 
        if q <= n:
            return q-1
        else:
            return min(n,2*n-q+1)

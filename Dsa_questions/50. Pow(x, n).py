class Solution:
    def myPow(self, x: float, n: int) -> float:
        ans = 1.0
        nn = n #for handling if the num is negative
        if nn < 0:
            nn = -1 * nn
        while nn:
            if nn % 2 == 0: # if nn is even 
                x = x*x
                nn //= 2
            else: # if nn is odd
                ans = ans * x
                nn -=1  
        if n < 0: # if n is negative as a power of x
            ans = 1.0 / ans
        return ans

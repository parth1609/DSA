
#Complete this function
class Solution:
    def floorSqrt(self, n): 
        low = 1
        high = n
        ans = 0
        while low <= high:
            mi = (low + high) // 2
            if (mi * mi) <= n:
                ans = mi
                low = mi + 1
            else:
                high = mi -1
        return ans

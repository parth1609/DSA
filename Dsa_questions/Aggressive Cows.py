
class Solution:
    def CanWePlace(self, stalls,distance,cows):
        total_cows = 1
        last_cow = stalls[0]
        for i in range(len(stalls)):
            if(stalls[i]-last_cow) >= distance:
                total_cows += 1
                last_cow = stalls[i]
                if total_cows == cows:
                    return True
        return False
        
    def aggressiveCows(self, stalls, k):
        stalls.sort()
        low = 1
        high = max(stalls) - min(stalls)
        while low <= high:
            mid = (low+high)//2
            if self.CanWePlace(stalls,mid,k):
                low = mid + 1
            else:
                high = mid - 1
        return high
        


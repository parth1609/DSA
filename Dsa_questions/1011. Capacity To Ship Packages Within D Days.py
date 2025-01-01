class Solution:
    def minimum_days(self, capacity, weights):
        min_days = 1
        load = 0
        for i in range(len(weights)):
            if load + weights[i] > capacity:
                min_days += 1
                load  = weights[i]
            else:
                load += weights[i]
        return min_days

    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights) # minimum capcity of ship
        right = sum(weights) # the capcity, by which all weights ship in one day
        while left <= right:
            mid = (left + right) // 2
            if self.minimum_days(mid,weights) <= days:
                right = mid - 1
            else:
                left = mid + 1
        return left


explain 

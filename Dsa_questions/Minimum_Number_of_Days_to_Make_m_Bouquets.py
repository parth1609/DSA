# 1482. Minimum Number of Days to Make m Bouquets


class Solution:
    # to find the minimum days to make 'm' bouquets 
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m * k > len(bloomDay):
            return -1

        def canWeMakeBouquets(day):
            bouquets = 0
            flowers = 0

            for bloom_at_that_day in bloomDay:
                if bloom_at_that_day <= day:
                    flowers += 1
                    if flowers == k:
                        bouquets += 1
                        flowers = 0
                else:
                    flowers = 0
                
                if bouquets == m:
                    return True

            return False

        left = min(bloomDay)
        right = max(bloomDay)

        while left < right:
            mid = (left + right) // 2
            if canWeMakeBouquets(mid):
                right = mid
            else:
                left = mid + 1

        return left

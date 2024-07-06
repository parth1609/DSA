class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        index = 1
        direction = 1 # right direction
        while time > 0:
            if (index + direction) >= 1 and (index + direction) <= n:
                index += direction
                time -=1
            else:
                direction *= -1 # left direction
            
        return index

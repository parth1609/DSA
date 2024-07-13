class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        total_bottle = numBottles
        while numBottles >= numExchange:
            new_bottles = numBottles // numExchange
            remaining_bottle = numBottles % numExchange 
            total_bottle += new_bottles
            numBottles = new_bottles + remaining_bottle
        return total_bottle


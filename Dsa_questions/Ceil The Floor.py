class Solution:
    def getFloorAndCeil(self, x: int, arr: list) -> list:
        # code here
        floor = float("-inf")
        ceil = float("inf")
        for num in arr:
            if num <= x:
                floor = max(floor,num)
            if num >= x:
                ceil = min(ceil,num)
        floor = -1 if floor==float("-inf") else floor 
        ceil = -1 if ceil==float("inf") else ceil 
        
        return floor,ceil
                

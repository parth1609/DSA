# Find maximum volume of a cuboid


class Solution:
    def maxVolume(self, perimeter, area):
        length = ((perimeter)-(((perimeter*perimeter)-24*area))**0.5)/12.0

        # Calculate volume
        volume = length * length * ((perimeter / 4) - 2 * length)
        
        return round(volume,2) 

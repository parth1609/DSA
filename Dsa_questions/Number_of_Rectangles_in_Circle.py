# Number of Rectangles in a Circle

class Solution:
    def rectanglesInCircle(self,r):
        #code here
        total_rectangle = 0
        diameter=2*r
        diametersq = diameter * diameter 
        
        for a in range(1,diameter + 1):
            for b in range(1,diameter + 1):
                if (a*a + b*b) <= diametersq:
                    total_rectangle+=1
        return total_rectangle

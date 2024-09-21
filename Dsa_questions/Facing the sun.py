
class Solution:
    # Returns count buildings that can see sunlight
    def countBuildings(self, height):
        # code here
        count = 1
        able_to_see = height[0]
        for i in range(1,len(height)):
            if height[i] > able_to_see:
                able_to_see = height[i]
                count += 1
        return count 

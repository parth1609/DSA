class Solution:
    #Function to return the position of the first repeating element.
    def firstRepeated(self,arr):
        
        #arr : given array
        #n : size of the array
        seen = set()
        repeated_index = float('inf')
        
        for i in range(len(arr)-1,-1,-1):
            if arr[i] in seen:
                repeated_index = i
            else:
                seen.add(arr[i])
        if repeated_index == float('inf'):
            return -1
        return repeated_index + 1

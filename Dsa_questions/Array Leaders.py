class Solution:
    #Back-end complete function Template for Python 3
    
    #Function to find the leaders in the array.
    def leaders(self,n, arr):
        #Code here
        leaders_array = []
        leader_from_right = arr[-1]
        leaders_array.insert(0,leader_from_right)
        
        for i in range(n-2,-1,-1):
            if leader_from_right <= arr[i] :
                leader_from_right = arr[i]
                leaders_array.insert(0,arr[i])
        
        return leaders_array
            

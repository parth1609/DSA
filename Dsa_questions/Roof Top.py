class Solution:
    
    #Function to find maximum number of consecutive steps 
    #to gain an increase in altitude with each step.
    def maxStep(self, arr):
        #Your code here
        
        top = 0
        maxtop = 0
        for i in range(1,len(arr)):
            if  arr[i-1] < arr[i]:
                top+=1
            else:
                top =0
                
            maxtop = max(top,maxtop)
        
        return maxtop
            

class Solution:
    #Function to rotate an array by d elements in counter-clockwise direction. 
    def rotateArr(self, arr, d):
        #Your code here
        n = len(arr)
        d = d % n
        
        # reverse until d-1
        self.reverse(arr, 0, d-1)
        
        # reverse from d-1
        self.reverse(arr,d,n-1)
        
        # reverse the array 
        self.reverse(arr,0,n-1)
        
        
       
    def reverse(self, arr, start, last):
        while start < last:
            arr[start], arr[last] = arr[last], arr[start]
            start+=1
            last -= 1
            
            

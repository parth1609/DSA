class Solution:
    def alternateSort(self,arr):
        # Your code goes here
        arr.sort()
        num = []
        i = 0
        j = len(arr) -1
        while i < j:
            num.append(arr[j])
            j-=1
            num.append(arr[i])
            i+=1
        if len(arr) % 2 == 1:
            num.append(arr[i])
          
        return num
            
            
            

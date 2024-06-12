# Sort Colors

class Solution:
    def sort012(self,arr,n):
        # code here
        low = 0
        mi = 0
        high = n-1
        
        while mi <= high:
            if arr[mi] == 0:
                arr[low],arr[mi] = arr[mi],arr[low]
                low+=1
                mi+=1
            elif arr[mi] == 1:
                mi+=1
            
            else : # arr[mi] == 2
                arr[mi],arr[high] = arr[high],arr[mi]
                high-=1
                
        return arr
                

class Solution:
    def segregate0and1(self, arr):
        # code here
        n = len(arr)
        low = 0
        high = n - 1
        
        while low < high:
            while arr[low] == 0 and low < high:
               low+=1
            while arr[high]==1 and low < high:
                high-=1
            if low < high:
                arr[low],arr[high] = arr[high],arr[low]
                low+=1
                high -= 1
        return arr

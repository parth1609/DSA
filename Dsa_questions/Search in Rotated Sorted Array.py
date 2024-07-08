
class Solution:
    def search(self,arr,key):
        # Complete this function
        left = 0 
        right  = len(arr)-1
        while left <= right:
            mi = ( left + right)//2
            if arr[mi] == key:
                return mi
            
            # for left sort array
            if arr[left] <= arr[mi]:
                if arr[left] <= key < arr[mi]:
                    right = mi -1
                else:
                    left= mi +1
            # for right sorted array
            else:
                if arr[mi] < key <= arr[right]:
                    left = mi + 1
                else:
                    right = mi - 1
        return -1
                

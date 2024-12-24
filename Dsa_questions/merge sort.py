
class Solution:
    def merge(self,arr,low,mid,high):
        left = low
        right = mid+1
        tmp = []
        while (left <= mid and right <= high):
            if (arr[left] <= arr[right]):
                tmp.append(arr[left])
                left+=1
            else:
                tmp.append(arr[right])
                right+=1
        
        while left <= mid:
            tmp.append(arr[left])
            left+=1
        while right <= high:
            tmp.append(arr[right])
            right+=1
            
        for i in range(low,high+1):
            arr[i] = tmp[i-low]
 
    def mergeSort(self,arr, left, right):
        #code here
        if (left>=right):
            return 
        mid = (left + right) // 2
        # to devide the array with recursion
        self.mergeSort(arr,left, mid)
        self.mergeSort(arr,mid+1,right)
        # to merge the array which is divide at every step
        self.merge(arr,left,mid,right)
        

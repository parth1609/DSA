class Solution:
    #User function Template for python3
    #Function to count inversions in the array.
    
    def merge(self,arr,low,mid,high):
        left = low
        right = mid+1
        tmp = []
        # declare cnt variable
        cnt = 0
        while (left <= mid and right <= high):
            if (arr[left] <= arr[right]):
                tmp.append(arr[left])
                left+=1
            else:
                tmp.append(arr[right])
                cnt += (mid-left+1)
                right+=1
        
        while left <= mid:
            tmp.append(arr[left])
            left+=1
        while right <= high:
            tmp.append(arr[right])
            right+=1
            
        for i in range(low,high+1):
            arr[i] = tmp[i-low]
        return cnt
 
    def mergeSort(self,arr, left, right):
        #code here
        cnt = 0
        if (left>=right):
            return cnt
        mid = (left + right) // 2
        # to devide the array with recursion
        cnt += self.mergeSort(arr,left, mid)
        cnt += self.mergeSort(arr,mid+1,right)
        # to merge the array which is divide at every step
        cnt += self.merge(arr,left,mid,right)
        
        return cnt
        
    def inversionCount(self, arr):
        # Your Code Here
        return self.mergeSort(arr,0, len(arr)-1)


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

    def countPairs(self,arr,low, mid,high):
        right = mid+1
        cnt = 0
        for i in range(low,mid+1):
            while right <= high and arr[i] > 2*arr[right]:
                right += 1
            cnt += (right - (mid+1))
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

        cnt += self.countPairs(arr, left,mid, right)
        # to merge the array which is divide at every step
        self.merge(arr,left,mid,right)
        return cnt
        
    def reversePairs(self, nums: List[int]) -> int:
        return self.mergeSort(nums,0,len(nums)-1)
        

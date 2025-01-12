class Solution:
    def CanWeAllocateMinimumPages(self,arr,pages):
        allocate_page = 0
        student = 1
        for i in range(len(arr)):
            if (allocate_page + arr[i]) <= pages:
                allocate_page += arr[i]
            else:
                student += 1
                allocate_page = arr[i]
        return student
        
    def findPages(self, arr, k):
        if k > len(arr):
            return -1
        low = max(arr)
        high = sum(arr)
        while low<=high:
            mid = (low+high) // 2
            if self.CanWeAllocateMinimumPages(arr,mid) <= k:
                high = mid-1
            else:
                low = mid + 1
        return low
                
        

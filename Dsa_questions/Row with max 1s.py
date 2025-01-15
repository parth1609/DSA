class Solution:
    def Find_first_occurance_of(self,arr):
        low = 0
        high = len(arr)-1
        count_ones = -1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == 1:
                count_ones = len(arr) - mid
                high = mid - 1
            elif arr[mid] == 0:
                low = mid + 1
            else:
                high = mid - 1
        return count_ones
                
    def rowWithMax1s(self, arr):
        # code here
        count_max = 0
        index = -1
        for i in range(len(arr)):
            count_ones = self.Find_first_occurance_of(arr[i])
            if count_max < count_ones:
                count_max = count_ones
                index = i
        return index

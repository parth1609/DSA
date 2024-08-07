
class Solution:
    def kthElement(self, k, arr1, arr2):
        arr1.extend(arr2)
        arr1.sort()
        return arr1[k-1]
        
        

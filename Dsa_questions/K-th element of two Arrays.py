
class Solution:
    def select_from_array(self,array, index, k):
        k-=1
        if k==0:
            return array[index],k
        return None,k

    def kthElement(self, a, b, k):
        left = 0
        right = 0
        result = -1
        while k > 0:
            if left < len(a) and (right >= len(b) or a[left] <= b[right]):
                result, k = self.select_from_array(a,left,k)
                if result is  None:
                    left += 1
            elif right < len(b):
                result, k = self.select_from_array(b,right,k)
                if result is None:
                    right += 1
                
        return result
                
            

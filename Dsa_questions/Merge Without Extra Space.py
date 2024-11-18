class Solution:
    def mergeArrays(self, a, b):
        # code here
        n = len(a)
        m = len(b)
        left  = n-1
        right = 0
        while left>=0 and right < m:
            if a[left] >= b[right]:
                a[left], b[right] = b[right], a[left]
                left -= 1
                right += 1
            else:
                break 
        a.sort()
        b.sort()
         

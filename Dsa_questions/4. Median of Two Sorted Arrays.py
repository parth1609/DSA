class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Ensure nums1 is the smaller array for binary search
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)
        
        n1, n2 = len(nums1), len(nums2)

        # Handle cases where one of the arrays is empty
        if n1 == 0:
            if n2 % 2 == 1:  # Odd length
                return nums2[n2 // 2]
            else:  # Even length
                return (nums2[(n2 // 2) - 1] + nums2[n2 // 2]) / 2.0

        n = n1+n2
        left = (n1+n2+1)//2
        
        low , high = 0, n1
        while low <= high:
            mid1 = (low + high) // 2
            mid2 = left - mid1

            l1,l2 = float('-inf'),float('-inf')
            r1,r2 = float('inf'),float('inf')

            # if mid1 or mid2 will be less than size
            # of n1 and resp.
            if mid1 < n1:
                r1 = nums1[mid1]
            if mid2 < n2:
                r2 = nums2[mid2]
            
            # when the mid1 and mid2 is greater than 0
            if mid1 - 1 >= 0:
                l1 = nums1[mid1 - 1]
            if mid2 - 1 >= 0:
                l2 = nums2[mid2 - 1]
            

            if l1 <= r2 and l2 <= r1:
                if n%2==1:
                    return max(l1,l2)
                else:
                    return (float(max(l1,l2)) + float(min(r1,r2))) / 2.0
            
            elif l1 > r2:
                high = mid1 -1
            else:
                low = mid1 + 1

        return 0.0 #nothing happens
            

            

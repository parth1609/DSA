class Solution:
    def greater_number(self, num, nums2):
        greatestElement = -1
        stack = []
        for i in range(len(nums2)-1,-1,-1):
            if nums2[i] == num:
                if stack and stack[-1] > num:
                    greatestElement = stack[-1]
                elif stack and stack[-1] <= num:
                    while stack and stack[-1] <= num:
                        stack.pop()
                    if stack and stack[-1] > num:
                        greatestElement = stack[-1]
            stack.append(nums2[i]) 
        return greatestElement

    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums1)):
            ans.append(self.greater_number(nums1[i], nums2))
        return ans

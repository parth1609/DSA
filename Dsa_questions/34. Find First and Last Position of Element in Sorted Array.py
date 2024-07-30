class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def binary_Search(nums,target,is_left):
            left = 0
            right = len(nums)-1
            i = -1
            while left <= right:
                mi = (left + right)//2
                if nums[mi] < target:
                    left = mi +1
                elif nums[mi] > target:
                    right = mi - 1
                else:
                    i = mi
                    if is_left:
                        right = mi - 1
                    else:
                        left = mi + 1
            return i

        left  = binary_Search(nums,target,True)
        right  = binary_Search(nums,target,False)
        return [left,right]
       

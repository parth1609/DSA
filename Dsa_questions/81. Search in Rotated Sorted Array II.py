class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left = 0
        right = len(nums)-1
        while left <= right:
            mi = (left+right)//2
            if nums[mi] == target:
                return True
            
            if nums[left] == nums[mi] and nums[mi] == nums[right]:
                left +=1
                right -= 1
                continue 
             
            elif nums[left] <= nums[mi]:
                if nums[left] <= target < nums[mi]:
                    right = mi - 1
                else:
                    left = mi + 1

                    
            elif nums[mi] <= nums[right]:
                if nums[mi] < target <= nums[right]:
                    left = mi + 1
                else:
                    right = mi -1
            else:
                left += 1
        return False 
                     

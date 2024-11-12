class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        nums.sort()
        for i in range(n):
            # for i, when there are duplicate itm then 
            # i incremented until the previous is not different 
            if i!=0 and nums[i] == nums[i-1]:
                continue 
            j = i+1
            k = n-1
            while j<k:
                Triplet_sum = nums[i] + nums[j] + nums[k]
                if Triplet_sum < 0:
                    j+=1
                elif Triplet_sum > 0:
                    k-=1
                else:
                    tmp = [nums[i],nums[j], nums[k]]
                    ans.append(tmp)
                    j+=1
                    k-=1

                    # skip all the diplicate element 
                    while j<k and nums[j] == nums[j-1]:
                        j+=1
                    while j<k and nums[k] == nums[k+1]:
                        k-=1

        return ans
 

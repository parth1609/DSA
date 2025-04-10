class Solution:
    def all_Subsets(self,arr,i,current,result):
        if i == len(arr):
            result.append(current[:])
            return
        current.append(arr[i])
        self.all_Subsets(arr,i+1,current,result)
        current.remove(arr[i])
        self.all_Subsets(arr,i+1,current,result)

    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.all_Subsets(nums,0,[],result)
        return result

class Solution:
    def Combination(self,ind,target,ds,ans,arr):
        if target==0:
            ans.append(ds[:])
            return
        for i in range(ind,len(arr)):
            if i > ind and arr[i]==arr[i-1]:
                continue
            if arr[i]>target:
                break
            ds.append(arr[i])
            self.Combination(i+1,target-arr[i],ds,ans,arr)
            ds.pop()
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        self.Combination(0,target,[],ans,candidates)
        return ans

class Solution:
    def combination(self,i,target,arr,ans,ds):
        if i==len(arr):
            if target==0:
                ans.append(ds.copy())
            return
        if arr[i] <= target:
            ds.append(arr[i])
            self.combination(i,target-arr[i],arr,ans,ds)
            ds.remove(arr[i])
        self.combination(i+1,target,arr,ans,ds)
        
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        self.combination(0,target,candidates,ans,[])
        return ans

class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        number_in_order = {}
        nums = sorted(set(arr))
        rank = 1
        for num in nums:
            number_in_order[num] = rank 
            rank +=1
        
        for i in range(len(arr)):
            arr[i] = number_in_order[arr[i]]

        return arr

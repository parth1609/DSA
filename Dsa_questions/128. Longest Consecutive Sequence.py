class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        count  = 0
        longest  = 1
        
        st = set()
        for i in range(n):
            st.add(nums[i]) 

        for num in st:
            if num - 1 not in st:
                count  = 1
                no = num
                while no + 1 in st:
                    no += 1
                    count += 1
                longest  = max(longest,count)
        return longest 



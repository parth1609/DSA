class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        n = len(nums)
        target = sum(nums) % p
        if target == 0:
            return 0

        mapp = {0: -1}
        current_sum = 0
        min_len = n
        for i in range(n):
            current_sum = (current_sum + nums[i]) % p
            needed = (current_sum - target + p) % p
            if needed in mapp:
                min_len = min(min_len, i - mapp[needed])
            mapp[current_sum] = i

        return -1 if min_len == n else min_len

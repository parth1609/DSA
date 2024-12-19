class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []
        result = prices[:] #copy the original array 

        for i in range(len(prices)):
            while stack and prices[stack[-1]] >= prices[i]:
                index = stack.pop()
                result[index] -= prices[i]
            stack.append(i)
        return result

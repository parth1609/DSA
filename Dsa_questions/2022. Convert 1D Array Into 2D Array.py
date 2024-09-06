class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        length = len(original)
        if m * n ==  length:
            result_array = [[0] * n for _ in range(m)]

            for i in range(length):
                row = i//n
                kol = i % n
                result_array[row][kol] = original[i]

            return  result_array
        return []
        

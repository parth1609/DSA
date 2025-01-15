class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix) #rows
        m = len(matrix[0]) #cols
        row = 0
        col = m-1
        while row < n and col >= 0:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                col -= 1
            else: # matrix[row][col] < target
                row += 1
        return False

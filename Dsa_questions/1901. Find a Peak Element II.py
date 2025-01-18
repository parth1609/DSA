class Solution:   
    def max_element_row(self,n,m,mat,col):
        maxi = -1
        ind = -1
        for i in range(n):
            if mat[i][col] > maxi:
                maxi = mat[i][col]
                ind = i
        return ind
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        n = len(mat) #total rows
        m = len(mat[0]) #total columns
        low = 0 
        high = m-1
        while low <= high:
            mid = (low + high) // 2
            row = self.max_element_row(n,m,mat,mid)
            left = mat[row][mid - 1] if mid - 1 >= 0 else -1
            right = mat[row][mid + 1] if mid + 1 < m else -1

            if left < mat[row][mid] > right:
                return [row,mid]
            
            elif left > mat[row][mid]:
                high = mid - 1
            else:
                low = mid + 1
        return [-1,-1] 

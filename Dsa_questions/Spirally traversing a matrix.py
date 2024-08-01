class Solution:
    # Function to return a list of integers denoting spiral traversal of matrix.
    def spirallyTraverse(self, matrix):
        # code here
        row = len(matrix)
        kol = len(matrix[0])
        
        top = 0
        bottom = row - 1
        left = 0
        right = kol - 1
        li = []
        while top<=bottom and left<=right:
            
            for i in range(left, right+1):
                li.append(matrix[top][i])
            top+=1
            
            for i in range(top , bottom+1):
                li.append(matrix[i][right])
            right-=1
            
            if top <= bottom :
                for i in range(right , left-1 ,-1):
                    li.append(matrix[bottom][i])
                bottom-=1
           
            if left <= right:
                for i in range(bottom,top-1,-1):
                    li.append(matrix[i][left])
                left += 1
        
        return li
        

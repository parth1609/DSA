# Left Rotate Matrix K times

class Solution:
    def rotateMatrix(self, k, mat):
        n = len(mat)
        m = len(mat[0])
        
        k = k % m  # Ensure k is within the row length
        
        if k != 0:
            for row in mat:
                for i in range(k):
                    pops = row.pop(0)
                    row.append(pops)
        
        return mat

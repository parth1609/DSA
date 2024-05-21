# Print 1 To N Without Loop

class Solution:    
    #Complete this function
    def printNos(self,N):
        # this is is rcursion technique to print the numbers 
        if N>0:
        # the printNos() fun is called repeatedly until n become 0
            self.printNos(N-1)
            print(N,end=" ")

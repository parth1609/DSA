class Solution:
    # Function to find the next greater element for each element of the array.
    def nextLargerElement(self, arr):
        stack = []
        result = []
        n = len(arr)
        for i in range(n-1,-1,-1):
            # if stack is not empty
            # remove top element of stack if
            # top element <= current ith element in array
            while stack and stack[-1] <= arr[i]:
                stack.pop()
                
            # if stack is empty
            if not stack:
                result.append(-1)
            else: # if stack is not empty
                result.append(stack[-1])
            
            stack.append(arr[i])
            

                    
        return result[::-1]
            

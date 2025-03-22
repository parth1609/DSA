class Solution:
    def delete_Element(self, stack, k):
        if k==0:
            stack.pop()
            return
        val = stack.pop()
        self.delete_Element(stack,k-1)
        stack.append(val)
        
        
    def deleteMid(self, stack):
        k = len(stack)//2
        self.delete_Element(stack,k)
        return stack
        

from typing import List

class Solution:
    def Insert(self,stack,ele):
        if len(stack)==0:
            stack.append(ele)
            return
        tmp = stack.pop()
        self.Insert(stack,ele)
        stack.append(tmp)
        
    def reverse(self,St): 
        n = len(St)
        if n==1:
            return
        tmp = St.pop()
        self.reverse(St)
        self.Insert(St,tmp)
        return St

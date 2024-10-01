'''
class node:
    def __init__(self):
        self.data = None
        self.next = None
'''

class Solution:
    def multiply_two_lists(self, first, second):
        # Code here
        m = 1000000007
        num1=num2=0
        while first is not None:
            num1 = ((num1*10)+first.data)%m
            first = first.next
        while second is not None:
            num2 = ((num2*10)+second.data)%m
            second = second.next 
        return (num1*num2)%m

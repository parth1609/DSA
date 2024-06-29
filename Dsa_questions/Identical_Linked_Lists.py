# Identical Linked Lists

'''
# Node Class    
class node:
    def __init__(self, val):
        self.data = val
        self.next = None
        
'''

#Function to check whether two linked lists are identical or not.
def areIdentical(head1, head2):
    # Code here
    tmp1 = head1
    tmp2 = head2
    while tmp1 and tmp2:
        if tmp1.data != tmp2.data :
            return False 
        tmp1 = tmp1.next 
        tmp2 = tmp2.next 
    
    if tmp1 is None and tmp2 is None:
        return True
    
    return False 

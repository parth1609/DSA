# linked_list_of_strings_forms_a_palindrome


'''
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
'''
def compute(head): 
    #return True/False
    string = ""
    while head:
        string += head.data
        head = head.next
    
    return string == string[::-1] 

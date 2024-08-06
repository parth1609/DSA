class Solution:
    def isValid(self, string):
        #code here
        parts = string.split(".")
        if  len(parts) != 4:
            return False 
           
        for part in parts:
            if not self.valid_part(part):
                return False 
        return True
        
    def valid_part(self, part):
        if not part.isdigit():
            return False
        
        num = int(part)
        
        if num <0 or num > 255 or (part[0] == "0" and len(part) > 1):
            return False 
        
        return True      

class Solution:
    def kPangram(self,string, k):
        
        string = string.replace(" ","")
        setstring = set(string)
        if len(string) < 26:
            return False 
        kth_string = 26 - len(setstring)
        
        return kth_string <= k

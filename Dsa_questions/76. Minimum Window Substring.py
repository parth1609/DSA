class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t) or not t or not s:
            return ""
        if s==t:
            return s
        t_map = {}
        for char in t:
            if char not in t_map:
                t_map[char] = 1
            else:
                t_map[char] += 1

        required = len(t_map)
        minlen = float('inf')
        min_window = ""
        formed = 0
        i=0
        for j in range(len(s)):
            if s[j] in t_map:
                t_map[s[j]] -= 1
                if t_map[s[j]] == 0:
                    formed += 1
            
            while formed == required and i <= j:
                if j - i + 1 < minlen:
                    minlen = j - i + 1
                    min_window = s[i:j + 1]
                
                if s[i] in t_map:
                    t_map[s[i]] += 1
                    if t_map[s[i]] > 0:
                        formed -= 1
                i += 1
                    
            
        return min_window
            



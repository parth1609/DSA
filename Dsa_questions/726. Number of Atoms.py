import collections
class Solution:
    def countOfAtoms(self, formula: str) -> str:
        def multiply_count(counts,factor):
            return {element: cnt * factor for element,cnt in counts.items() }
        
        stack = []
        current_kount = collections.defaultdict(int)
        n = len(formula)
        i =0
        while i < n:
            if formula[i] == "(":
                stack.append(current_kount)
                stack.append("(")
                current_kount = collections.defaultdict(int)
                i+=1
            elif formula[i] == ")":
                i += 1
                num_start = i
                while i < len(formula) and formula[i].isdigit():
                    i += 1
                multiplier = int(formula[num_start:i] or 1)
                current_kount  = multiply_count(current_kount,multiplier)
                # pop "(" from stak
                stack.pop()
                prv = stack.pop()
                for element,count in current_kount.items():
                    prv[element] += count 
                current_kount = prv
                
            else:
                start = i
                i +=1
                while i<n and formula[i].islower():
                    i+=1
                element = formula[start:i]
                num_start = i
                while i<n and formula[i].isdigit():
                    i+=1
                count = int(formula[num_start:i] or 1)
                current_kount[element] += count 
                
        sorted_elements = sorted(current_kount.items())
        return ''.join(f"{element}{kounts if kounts > 1 else ''}" for element,kounts in sorted_elements)

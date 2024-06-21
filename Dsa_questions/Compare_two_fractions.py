# Compare two fractions

class Solution:
    def compareFrac(self, string: str) -> str:
        # Split the input string into two fractions
        txt = string.split(", ")
        
        # Split each fraction into numerator and denominator
        a, b = map(int, txt[0].split("/"))
        c, d = map(int, txt[1].split("/"))
        
        # Compare the fractions
        fraction1 = a / b
        fraction2 = c / d
        
        if fraction1 == fraction2:
            return "equal"
        elif fraction1 > fraction2:
            return txt[0]
        else:
            return txt[1]

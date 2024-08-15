class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fiveDollarBills = 0
        tenDollarBills = 0
        for bill in bills:
            if bill == 5:
                fiveDollarBills += 1
            elif bill == 10:
                tenDollarBills += 1
                if fiveDollarBills > 0:
                    fiveDollarBills -=1
                else:
                    return False 
            elif bill == 20:
                if fiveDollarBills > 0 and tenDollarBills > 0:
                    fiveDollarBills -=1 
                    tenDollarBills -=1 
                elif fiveDollarBills >= 3:
                    fiveDollarBills-=3
                else:
                    return False 

        return True
                
    
            
        

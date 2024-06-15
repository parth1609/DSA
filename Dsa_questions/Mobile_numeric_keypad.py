# Mobile numeric keypad

#User function Template for python3
class Solution:
    def get_moves(self):
        return {
            '0': ['0', '8'],
            '1': ['1', '2', '4'],
            '2': ['2', '1', '3', '5'],
            '3': ['3', '2', '6'],
            '4': ['4', '1', '5', '7'],
            '5': ['5', '2', '4', '6', '8'],
            '6': ['6', '3', '5', '9'],
            '7': ['7', '4', '8'],
            '8': ['8', '5', '7', '9', '0'],
            '9': ['9', '6', '8']
    }
    def count_number(self, digit,length, moves, memo):
        if length == 1:
            return 1
            
        if (digit, length) in memo:
            return memo[(digit, length)]
            
        total_count = 0
        for move in moves[digit]:
            total_count += self.count_number(move, length - 1, moves, memo)
        
        memo[(digit, length)] = total_count
        return total_count
        
	def getCount(self, n):
		
		if n == 0:
		    return 1
		if n == 1:
		    return 10
        
        moves = self.get_moves()
        total_count = 0
        memo = {}
        
		for digit in '0123456789':
		    total_count += self.count_number(digit,n,moves,memo)
		
		return total_count 



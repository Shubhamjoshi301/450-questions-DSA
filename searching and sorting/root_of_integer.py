import math
class Solution:
    def countSquares(self, N):
        # code here 
        n = math.sqrt(N)
        if n%1 == 0:
            
            return int(n-1)
        else: return int(n) 
        

import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        L, R = 1, max(piles)
        minSpeed = max(piles)
        while L <= R:
            numHours = 0
            M = (L + R) // 2
                
            for bananas in piles:
                numHours += math.ceil(bananas / M)
            
            if numHours <= h:
                minSpeed = min(M, minSpeed)
                R = M - 1
            else:
                L = M + 1
        return minSpeed

    #    speeds = [1 ... 25]
    #    L = 19, R = 24
    #    minSpeed = 19
    #    M = 21
    #    speeds[M] = 19
    #    numHours = 0
    

            
            
            
                    
                
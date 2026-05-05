class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n < 0:
            x = 1/x
            n = n*-1

        y = 1
        while n  > 0:
            if n % 2 == 1:
                y *= x
            x *= x
            n //= 2
        
        return y

#runtime: 0ms, beats 100%
#memory: 19.62MB, beats 19.61%
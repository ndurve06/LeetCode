import math

class Solution:
    def judgeSquareSum(self, c):
        for i in range(int(sqrt(c)) + 1):
            j = sqrt(c - i*i)
            if j == int(j):
                return True
        return False
    

#runtime: 70ms, beats 37.63%
#memory: 19.34MB, beats 57.66%
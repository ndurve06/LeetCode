class Solution:
    def isPowerOfTwo(self, n):
        if n == 0:
            return False
        return n == 1 or (n % 2 == 0 and self.isPowerOfTwo(n//2))

#runtime: 0ms, beats 100.00%
#memory: 19.37MB, beats 19.83%
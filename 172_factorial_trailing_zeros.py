class Solution:
    def trailingZeroes(self, n: int) -> int:
        zeros = 0
        while n > 0:
            n //= 5
            zeros += n
        return zeros
        

testing = Solution()
print(testing.trailingZeroes(30))

#runtime: 0ms, beats 100.00%
#memory: 19.22MB, beats 62.67%
class Solution:
    def arrangeCoins(self, n):
        i = 1
        while True:
            n = n - i
            if n == 0:
                return i
            if n < 0:
                return i - 1
            i = i + 1


testing = Solution()
print(testing.arrangeCoins(5))

#runtime: 592ms, beats 23.55%
#memory: 19.30MB, beats 30.12%
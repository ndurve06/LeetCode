class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        a = 0 
        b = 1
        c  = 0 
        for i in range(n - 1):
            c = a + b
            a, b = b, c
        return c

testing = Solution()
print(testing.fib(0))
print(testing.fib(30))
print(testing.fib(4))

#runtime: 45ms, beats 69.01%
#memory: 19.20MB, beats 57.40%
class Solution:
    def fizzBuzz(self, n):
        output = []
        for i in range(1, n +1):
            if i % 3 == 0 and i % 5 == 0:
                output.append("FizzBuzz")
            elif i % 3 == 0:
                output.append("Fizz")
            elif i % 5 == 0:
                output.append("Buzz")
            else:
                output.append(str(i))
        return output
    
testing = Solution()
print(testing.fizzBuzz(15))

#runtime: 0ms, beats 100.00%
#memory: 19.48MB, beats 86.54%
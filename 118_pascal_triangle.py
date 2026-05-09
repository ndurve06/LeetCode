import math

class Solution:
    def generate(self, numRows):
        result = []
        for j in range(numRows):
            row = []
            for i in range(0, j + 1):
                number = math.factorial(j) // (math.factorial(i) * math.factorial(j - i))
                row.append(number)
            result.append(row)
        return result
    
testing = Solution()
print(testing.generate(6))

#runtime: 0ms, beats 100.00%
#memory: 19.52MB, beats 6.43%
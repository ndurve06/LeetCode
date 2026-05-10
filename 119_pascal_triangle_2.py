import math

class Solution:
    def getRow(self, rowIndex):
        row = []
        for i in range(0, rowIndex+1):
            number = math.factorial(rowIndex) // (math.factorial(i) * math.factorial(rowIndex - i))
            row.append(number)
        return row
    
testing = Solution()
print(testing.getRow(3))

#runtime: 0ms, beats 100.00%
#memory: 19.40MB, beats 21.65%
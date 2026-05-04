class Solution:
    def searchMatrix(self, matrix, target):
        for i in range(len(matrix)):
            row = matrix[i]
            if target in row:
                return True
        return False


testing = Solution()
print(testing.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))

#runtime: 0ms, beats 100.00%
#memory: 19.52MB, beats 41.54%
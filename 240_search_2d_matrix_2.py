class Solution:
    def searchMatrix(self, matrix, target) -> bool:
        for i in range(len(matrix)):
            row = matrix[i]
            if target in row:
                return True
        return False

testing = Solution()
print(testing.searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 5))
print(testing.searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 20))

#runtime: 144ms, beats 47.61%
#memory: 25.62MB, beats 22.93%

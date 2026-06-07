class Solution:
    def distributeCandies(self, candyType):
        limit = len(candyType) // 2
        unique = len(set(candyType))
        if limit == unique:
            print("a")
            return limit
        elif limit > unique:
            print("b")
            return unique
        else:
            print("c")
            return limit


testing = Solution()
print(testing.distributeCandies([1,1,2,2,3,3]))
print(testing.distributeCandies([1,1,2,3]))
print(testing.distributeCandies([6,6,6,6]))

#runtime: 13ms, beats 86.57%
#memory: 21.08MB, beats 76.32%
class Solution:
    def findDuplicate(self, nums):
        found = set()
        
        for i in nums:
            if i in found:
                return i
            found.add(i)


testing = Solution()
print(testing.findDuplicate([1,3,4,2,2]))
print(testing.findDuplicate([3,1,3,4,2]))
print(testing.findDuplicate([3,3,3,3,3]))

#runtime: 18ms, beats 92.97%
#memory: 33.57MB, beats 47.67%
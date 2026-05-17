class Solution:
    def containsDuplicate(self, nums):
        nums_set = set(nums)
        if len(nums_set) == len(nums):
            return False
        else:
            return True

testing = Solution()
print(testing.containsDuplicate([1,2,3,1]))

#runtime: 5ms beats:91.24%
#memory:31.21MB beats:71.23%
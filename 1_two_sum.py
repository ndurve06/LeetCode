class Solution:
    def twoSum(self, nums, target):
        for i in range (len(nums)):
            for j in range (i + 1, len(nums)):
                total = nums[i] + nums[j]
                if total == target:
                    return [i, j]

testing = Solution()
print(testing.twoSum([3,2,4], 6))

#returns [0, 1] as expected

#runtime: 1886ms, beats 8.69%
#memory:19.89MB, beats 76.96%

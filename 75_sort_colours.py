class Solution:
    def sortColors(self, nums):
        for j in range(len(nums)):
            for i in range(1, len(nums)):
                if nums[i] < nums[i - 1]:
                    nums[i], nums[i - 1] = nums[i - 1], nums[i]

testing = Solution()
print(testing.sortColors([2,0,2,1,1,0]))
    
#runtime: 3ms, beats 10.82%
#memory: 19.29MB, 61.98%
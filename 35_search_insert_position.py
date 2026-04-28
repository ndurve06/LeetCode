class Solution:
    def searchInsert(self, nums, target):
        for i in range(len(nums)):
            if nums[i] == target:
                return i
        for i in range(1, len(nums)):
            if nums[i-1] <= target and nums[i] >= target:
                return i
        if nums[0] >= target:
            return 0
        if nums[-1] <= target:
            return len(nums)
        return -1

testing = Solution()
print(testing.searchInsert([1,3,5,6], 5))

#runtime: 0ms, beats 100%
#memory: 20MB, beats 17.28%
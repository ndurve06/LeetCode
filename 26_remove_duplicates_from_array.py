class Solution:
    def removeDuplicates(self, nums):
        k = 1
        for i in range (1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[k] = nums[i]
                k += 1
        return k

nums = [0,0,1,1,1,2,2,3,3,4]

testing = Solution()
print(testing.removeDuplicates(nums))

#runtime: 0ms, beats 100%
#memory: 20.43MB, beats 82.27%
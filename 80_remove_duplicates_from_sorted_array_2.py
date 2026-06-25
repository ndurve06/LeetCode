class Solution:
    def removeDuplicates(self, nums):
        output = len(nums)

        i = 2

        while i < len(nums):
            if nums[i] == nums[i-1] == nums[i-2]:
                nums.pop(i)
                output = output - 1
            else:
                i = i + 1
        
        return output


testing = Solution()
print(testing.removeDuplicates([1,1,1,2,2,3]))

#runtime: 100ms, beats 9.10%
#memory: 21.93MB, beats 73.85%
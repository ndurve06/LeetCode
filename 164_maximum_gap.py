class Solution:
    def maximumGap(self, nums):
        if len(nums) == 0:
            return 0
        nums.sort()
        max = 0
        for i in range(len(nums) - 1):
            diff = nums[i+1] - nums[i]
            if diff > max:
                max = diff
        
        return max

testing = Solution()
print(testing.maximumGap([3,6,9,1]))
print(testing.maximumGap([10]))

#runtime: 135ms, beats 88.14%
#memory: 31.90MB, beats 73.70%
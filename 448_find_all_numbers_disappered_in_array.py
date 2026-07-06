class Solution:
    def findDisappearedNumbers(self, nums):
        for n in nums:
            i = abs(n) - 1
            nums[i] = -abs(nums[i])
        return [i+1 for i in range(len(nums)) if nums[i] > 0]
    

#runtime: 48ms, beats 16.38%
#memory: 30.66MB, beats 64.50%
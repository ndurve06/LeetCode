class Solution:
    def findPeakElement(self, nums):
        if len(nums) == 1:
            return 0
        if nums[0] > nums[1]:
            return 0
        elif nums[-1] > nums[-2]:
            return len(nums) - 1
        for i in range(1, len(nums) - 1):
            if nums[i - 1] < nums [i] and nums [i] > nums [i + 1]:
                    return i
    
testing = Solution()
print(testing.findPeakElement([1,2,3,1]))
print(testing.findPeakElement([1,2,1,3,5,6,4]))
print(testing.findPeakElement([1,2,1,3,5,6,4,7]))
print(testing.findPeakElement([7,2,1,3,5,6,4]))

#runtime: 0ms, beats 100.00%
#memory: 19.34MB, beats 39.98%
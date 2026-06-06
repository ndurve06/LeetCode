class Solution:
    def singleNonDuplicate(self, nums):
        for i in range (0, len(nums)-1, 2):
            if nums[i] != nums[i+1]:
                return nums[i]
        return nums[-1]

testing = Solution()
print(testing.singleNonDuplicate([1,1,2,3,3,4,4,8,8]))
print(testing.singleNonDuplicate([3,3,7,7,10,11,11]))
print(testing.singleNonDuplicate([3,3,7,7,10,10,11]))
print(testing.singleNonDuplicate([3]))


#runtime: 2ms, beats 16.49%
#memory: 26.92MB, beats 61.20%
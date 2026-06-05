class Solution:
    def findKthLargest(self, nums, k):
        nums.sort()
        value = k*-1
        return nums[value]


testing = Solution()
print(testing.findKthLargest([3,2,1,5,6,4], 2))
print(testing.findKthLargest([3,2,3,1,2,4,5,5,6], 4))

#runtime: 47ms, beats 90.22%
#memory: 30.87.MB, beats 72.87%
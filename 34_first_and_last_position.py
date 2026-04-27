class Solution:
    def searchRange(self, nums, target):
        if nums == []:
            return [-1, -1]
        if target not in nums:
            return [-1, -1]
        positions = []
        for i in range (0, len(nums)):
            if nums[i] == target:
                positions.append(i)
        return [positions[0], positions[-1]]

testing = Solution()
print(testing.searchRange([5,7,7,8,8,8,10], 8))

#runtime: 0ms, beats 100%
#memory: 20.47MB, beats 91.83%
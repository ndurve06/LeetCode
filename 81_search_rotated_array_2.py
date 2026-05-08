class Solution:
    def search(self, nums, target):
        for i in range(len(nums)):
            if nums[i] == target:
                return True
        return False


#runtime: 0ms, beats 100.00%
#memory: 19.62MB, beats 33.33%

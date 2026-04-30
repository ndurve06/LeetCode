class Solution:
    def search(self, nums, target) -> int:
        for i in range(len(nums)):
            if nums[i] == target:
                return i 
        return -1
    

#runtime: 0ms, beats 100.00%
#memory: 19.46MB, beats 39.19%
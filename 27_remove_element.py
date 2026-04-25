class Solution:
    def removeElement(self, nums, val):
        counter = 0
        for i in range(len(nums)):
            if nums[i] == val:
                counter +=1
        while val in nums:
            nums.remove(val)
        print(nums)
        

nums = [3,2,2,3]
val = 3

testing = Solution()
testing.removeElement(nums, val)

#runtime: 0ms, beats 100%
#memory: 19.37MB, beats 28.50%
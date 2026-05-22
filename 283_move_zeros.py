class Solution:
    def moveZeroes(self, nums):
        i = 0
        n = len(nums)

        while i < n:
            if nums[i] == 0:
                nums.pop(i)
                nums.append(0)
                n -= 1
            else:
                i += 1

testing = Solution()
print(testing.moveZeroes([0,1,0,3,12]))

#runtime: 19ms, beats 10.71%
#memory: 20.46MB, beats 61.35%
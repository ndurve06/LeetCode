class Solution:
    def findMaxConsecutiveOnes(self, nums):
        count = 0
        max = 0
        if len(nums) == 0:
            return 0
        for i in range(len(nums)):
            if i == 0 and nums[i] == 1:
                count += 1
            elif nums[i] == 1:
                if nums[i-1] == 1:
                    count += 1
                else:
                    count = 1
            else:
                if count > max:
                    max = count
                count = 0

        if count > max:
            max = count 

        return max


testing = Solution()
print(testing.findMaxConsecutiveOnes([1,1,0,1,1,1]))
print(testing.findMaxConsecutiveOnes([1,0,1,1,0,1]))

#runtime: 28ms, beats 6.85%
#memory: 21.79MB, beats 79.89%
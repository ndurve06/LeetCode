class Solution:
    def threeSum(self, nums):
        nums.sort()
        result = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            j = i + 1
            k = len(nums) - 1

            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if total > 0:
                    k = k - 1
                elif total < 0:
                    j = j + 1
                else:
                    result.append([nums[i], nums[j], nums[k]])
                    j = j + 1
                    while nums[j] == nums[j-1] and j < k:
                        j = j + 1

        return result 
        

testing = Solution()
print(testing.threeSum([-1,0,1,2,-1,-4]))
print(testing.threeSum([0,1,1]))
print(testing.threeSum([0,0,0]))

#runtime: 611ms, beats 69.47%
#memory: 22.14MB, beats 81.24%
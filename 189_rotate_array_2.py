#More efficient
class Solution:
    def rotate(self, nums, k):
        length = len(nums)
        k = k % length
        rotation = (length - k)

        temp = nums[0:rotation]
        nums[0:rotation] = []
        nums.extend(temp)
        
        return nums
    

testing = Solution()
print(testing.rotate([1,2,3,4,5,6,7], 3))
print(testing.rotate([-1,-100,3,99], 2))
print(testing.rotate([1, 2], 7))

#runtime: 3ms, beats 75.80%
#memory: 24.48MB, beats 70.66%

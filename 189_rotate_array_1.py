#Less efficient
class Solution:
    def rotate(self, nums, k):
        nums_length = len(nums)
        if k > nums_length:
            k = k % nums_length 
            print(k)
        
        for i in range(k):
            rotate = nums[-1]
            nums.insert(0, rotate)
            nums.pop()
        
        return nums
    

testing = Solution()
print(testing.rotate([1,2,3,4,5,6,7], 3))
print(testing.rotate([-1,-100,3,99], 2))
print(testing.rotate([1, 2], 7))

#runtime: 1664ms, beats 8.65%
#memory: 23.39MB, beats 93.40%

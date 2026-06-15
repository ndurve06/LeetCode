class Solution:
    def merge(self, nums1, m, nums2, n) -> None:
        nums1[:] = nums1[:m] + nums2[:n]
        nums1.sort()
        #return nums1


testing = Solution()
print(testing.merge([1,2,3,0,0,0], 3, [2,5,6], 3))
print(testing.merge([1],1, [], 0))
print(testing.merge([0], 0, [1], 1))
        

#runtime: 0ms, beats 100.00%
#memory: 19.35MB, beats 39.05%
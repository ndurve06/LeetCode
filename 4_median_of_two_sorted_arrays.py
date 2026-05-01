class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        for i in range (len(nums2)):
            nums1.append(nums2[i])
        
        for j in range(len(nums1)):
            for i in range(1, len(nums1)):
                if nums1[i] > nums1[i - 1]:
                    nums1[i], nums1[i - 1] = nums1[i - 1], nums1[i]
        
        mp = len(nums1)
        if mp % 2 == 0:
            centre_2 = mp // 2
            centre_1 = centre_2 - 1
            median = (nums1[centre_2] + nums1[centre_1]) / 2
        else:
            centre = mp // 2
            median = nums1[centre]
        return float(median) 
    

testing = Solution()
print(testing.findMedianSortedArrays([1,2], [3,4]))

#runtime: 2952ms, beats 5.03%
#memory: 19.54MB, beats 42.95%

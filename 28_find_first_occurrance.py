class Solution:
    def strStr(self, haystack, needle):
        index = -1
        for i in range(len(haystack)):
            if haystack[i:i+len(needle)] == needle:
                index = i
                return index
        return index
    
haystack = "sadbutsad"
needle = "sad"

testing = Solution()
print(testing.strStr(haystack, needle))

#runtime: 2ms, beats 23.47%
#memory: 19.28MB, beats 66.66%
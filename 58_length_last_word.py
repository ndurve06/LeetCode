class Solution:
    def lengthOfLastWord(self, s):
        phrases = s.split()
        return len(phrases[-1])

testing = Solution()
print(testing.lengthOfLastWord("Hello World"))

#runtime: 0ms, beats 100.00%
#memory: 19.16MB, 87.92%
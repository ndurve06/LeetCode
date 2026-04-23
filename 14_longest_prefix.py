class Solution:
    def longestCommonPrefix(self, strs):
        letters = ""
        for i in range(len(strs[0])):
            char = strs[0][i]
            for phrase in strs:
                if i >=len(phrase) or phrase[i]!= char:
                    return letters
            letters += char
        return (letters)

testing = Solution()
print(testing.longestCommonPrefix(["flower","flow","flight"]))
        
class Solution:
    def firstUniqChar(self, s):
        counter = {}
        for letter in s:
            if letter in counter:
                counter[letter] += 1
            else:
                counter[letter] = 1
        
        for i in range(len(s)):
            if counter[s[i]] == 1:
                return i
            
        return -1

testing = Solution()
print(testing.firstUniqChar("leetcode"))
print(testing.firstUniqChar("loveleetcode"))
print(testing.firstUniqChar("aabb"))


#runtime: 87ms, beats 21.57%
#memory: 19.56MB, beats 89.12%
        
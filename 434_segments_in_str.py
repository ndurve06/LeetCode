class Solution:
    def countSegments(self, s):
        if s.isspace(): 
            return 0
        count = 0
        for i in range(0, len(s)):
            if s[i] != " " and (i == 0 or s[i - 1] == " "):
                count = count + 1
        
        return count


#runtime: 0ms, beats 100.00%
#memory: 19.17MB, beats 83.07%
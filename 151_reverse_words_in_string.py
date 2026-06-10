class Solution:
    def reverseWords(self, s: str) -> str:
        s.strip()
        word = s.split()
        reversed = word[::-1]
        output = " ".join(reversed)
        return output

#runtime: 0ms, beats 100.00%
#memory: 19.30MB, beats 41.21%
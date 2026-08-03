class Solution:
    def frequencySort(self, s) -> str:
        counter = {}
        for i in range(len(s)):
            if s[i] in counter:
                counter[s[i]] += 1
            else:
                counter[s[i]] = 1

        ordered = sorted(counter.items(), key=lambda x: x[1], reverse=True)

        output = ""
        for i in range(len(ordered)):
            output += ordered[i][0] * ordered[i][1]

        return output

testing = Solution()
print(testing.frequencySort("Aabb"))

#runtime: 14ms, beats 27.94%
#memory: 20.21MB, beats 41.02%

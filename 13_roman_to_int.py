class Solution:
    def romanToInt(self, s):
        conversion = {
            "I":1, 
            "V":5, 
            "X":10, 
            "L":50, 
            "C":100, 
            "D":500, 
            "M":1000
            }
        
        total = 0 
        for i in range(len(s)):
            current = s[i]
            if i !=0:
                previous = s[i-1]
                if conversion[current] > conversion[previous]:
                    total += conversion[current] - (2 * conversion[previous])
                else: 
                    total += conversion[current]
            else:
                total += conversion[current]
        return(total)

testing = Solution()
print(testing.romanToInt("MCMXCIV"))

#returns 1994 as expected
#runtime 4ms, beats 64.19%
#memory 19.18MB, beats 92.67%

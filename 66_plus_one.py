class Solution:
    def plusOne(self, digits):
        string_input = ""
        for i in range(len(digits)):
            string_input += str(digits[i])
        number = int(string_input)
        number += 1
        string_output = str(number)
        output = []
        for j in range(len(string_output)):
            output.append(int(string_output[j]))
        return output

testing = Solution()
print(testing.plusOne([1,2,3]))

#runtime: 0ms, beats 100%
#memory: 19.30MB, beats 57.57%
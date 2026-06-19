class Solution:
    def majorityElement(self, n):
        counter = {}
        output = []
        min = len(n) // 3
        for num in n:
            if num in counter:
                counter[num] += 1
            else:
                counter[num] = 1
        
        for i, j in counter.items():
            if j > min:
                output.append(i)

        return output
        
testing = Solution()
print(testing.majorityElement([3,2,3]))
print(testing.majorityElement([1]))
print(testing.majorityElement([1,2]))

#runtime: 8ms, beats 48.81%
#memory: 23.36MB, beats 35.09%
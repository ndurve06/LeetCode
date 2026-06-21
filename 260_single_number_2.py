class Solution:
    def singleNumber(self, nums):
        counter = {}
        output = []
        for num in nums:
            if num in counter:
                counter[num] += 1
            else:
                counter[num] = 1
        
        for i, j in counter.items():
            if j == 1:
                output.append(i)

        return output
    
#runtime: 4ms, beats 34.73%
#memory: 21.01MB, beats 23.83%
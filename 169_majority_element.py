class Solution:
    def majorityElement(self, nums):
        counter = {}
        output = 0
        for num in nums:
            if num in counter:
                counter[num] += 1
            else:
                counter[num] = 1

        ordered = sorted(counter.items(), key=lambda x: x[1], reverse=True)
        output = ordered[0][0]

        return output

#runtime: 13ms, beats 23.32%
#memory: 21.06MB, beats 87.75%
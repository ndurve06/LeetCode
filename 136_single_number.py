class Solution:
    def singleNumber(self, nums):
        counter = {}
        
        for num in nums:
            if num in counter:
                counter[num] += 1
            else:
                counter[num] = 1
        
        for i, j in counter.items():
            if j == 1:
                return i

testing = Solution()
print(testing.singleNumber([2,2,1])) #1
print(testing.singleNumber([4,1,2,1,2])) #4
print(testing.singleNumber([1])) #1

#runtime: 0ms, beats 100.00%
#memory: 21.55MB, beats 18.50%
class Solution:
    def firstMissingPositive(self, nums) -> int:
        positives = []
        for num in nums:
            if num > 0:
                positives.append(num)
        positives.sort()

        missing = 1

        for num in positives:
            if num == missing:
                missing = missing + 1
            elif num > missing:
                return missing
        
        return missing

testing = Solution()
print(testing.firstMissingPositive([1,2,0]))
print(testing.firstMissingPositive([3,4,-1,1]))
print(testing.firstMissingPositive([7,8,9,11,12]))

#runtime: 39ms, beats 70.11%
#memory: 30.77MB, beats 82.28%
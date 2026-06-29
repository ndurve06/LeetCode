class Solution:
    def singleNumber(self, nums) -> int:
        counter = {}
        
        for num in nums:
            if num in counter:
                counter[num] += 1
            else:
                counter[num] = 1
        
        for i, j in counter.items():
            if j == 1:
                return i
            
#runtime: 1ms, beats 81.45%
#memory: 20.84MB, beats 26.93%
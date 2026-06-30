import itertools

class Solution:
    def permute(self, nums):
        return list(itertools.permutations(nums))
    
#runtime: 0ms, beats 100.00%
#memory: 19.49MB, beats 65.32%
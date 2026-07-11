import itertools

class Solution:
    def permuteUnique(self, nums):
        return list(set(list((itertools.permutations(nums)))))

#runtime: 15ms, beats 21.76%
#memory: 24.82MB, beats 5.52%
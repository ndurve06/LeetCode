class Solution:
    def detectCapitalUse(self, word):
        if word.isupper():
            return True 
        elif word.islower():
            return True
        
        if word[0].isupper():
            if word[1:].islower():
                return True
            else:
                return False
        
        return False
                
testing = Solution()
print(testing.detectCapitalUse("ffffffffffffffffffffF"))

#runtime: 00ms, beats 100.00%
#memory: 19.48MB, beats 23.31%

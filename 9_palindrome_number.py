class Solution:
    def isPalindrome(self, x):
        if x < 0:
            return False
    
        string = str(x)
        reversed = ""

        for i in range(len(string) - 1, -1, -1):
            reversed = reversed + (string[i])
        
        if reversed == string:
            return True
        else:
            return False

testing = Solution()
print(testing.isPalindrome(134321))
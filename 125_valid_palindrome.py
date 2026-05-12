import string 

class Solution:
    def isPalindrome(self, s):
        s = s.lower()
        translator = str.maketrans('', '', string.punctuation)
        clean_text = s.translate(translator)
        clean_text = clean_text.replace(" ", "")
        rev = ""
        for i in range(len(clean_text) - 1, -1, -1):
            rev += clean_text[i]
        if clean_text == rev:
            return True
        else:
            return False

testing = Solution()
print(testing.isPalindrome("race a car"))

#runtime: 6ms, beats 84.72%
#memory: 19.72MB, beats 43.84%
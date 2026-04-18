class Solution:
    def reverse(self, x):
        int_str = str(x)
        negative = False
        rev = ""

        for i in range(len(int_str) -1 , -1, -1):
            if int_str[i] == "-":
                negative = True
                continue
            rev += int_str[i]
        if int(rev) < -2**31 or int(rev) >2**31 - 1:
            return 0
        if negative:
            return int("-"+rev)
        else:
            return int(rev)

testing = Solution()
print(testing.reverse(-123))

#runtime: 58ms, beats 5.07%
#memory: 19.27MB, beats 40.81%
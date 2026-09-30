class Solution:

    def __init__(self):
        self.data = []
        self.head = 0
        self.tail = -1

    def push(self, new_value):
        self.data.append(new_value)
        self.tail += 1

    def pop(self):
        if self.tail == -1:
            raise IndexError("Stack Empty")
        poped = self.data[-1]
        self.data.pop(-1)
        self.tail -= 1
        return poped

    def peek(self):
        if self.tail == -1:
            raise IndexError("Stack Empty")
        return self.data[-1]

    def length(self):
        return len(self.data)

    def isValid(self, s) -> bool:
        valid_pairs = {
            ')': '(',
            '}': '{', 
            ']': '['
            }
        for sign in s:
            if sign in valid_pairs.values():
                self.push(sign)
            elif sign in valid_pairs:
                if self.length() == 0 or self.peek() != valid_pairs[sign]:
                    return False
                self.pop()
        return not self.data


testing = Solution()
print(testing.isValid("()"))
print(testing.isValid("()[]{}"))
print(testing.isValid("(]"))
print(testing.isValid("([])"))
print(testing.isValid("([)]"))

#runtime: 0ms, beats 100%
#memory: 19.28MB, beats 64.64%


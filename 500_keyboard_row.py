class Solution:
    def findWords(self, words):
        row1 = ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p"]
        row2 = ["a", "s", "d", "f", "g", "h", "j", "k", "l"]
        row3= ["z", "x", "c", "v", "b", "n", "m"]

        output = []

        for word in words:
            temp = word
            word = word.lower()

            if word[0] in row1:
                valid = True
                for letter in word:
                    if letter not in row1:
                        valid = False
                        break
                if valid:
                    output.append(temp)
            
            if word[0] in row2:
                valid = True
                for letter in word:
                    if letter not in row2:
                        valid = False
                        break
                if valid:
                    output.append(temp)

            if word[0] in row3:
                valid = True
                for letter in word:
                    if letter not in row3:
                        valid = False
                        break
                if valid:
                    output.append(temp)
        
        return output

#runtime: 0ms, beats 100.00%
#memory: 19.30MB, beats 27.26%
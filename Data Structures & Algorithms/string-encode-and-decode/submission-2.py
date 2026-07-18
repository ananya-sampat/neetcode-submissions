#class Solution:
#
#    def encode(self, strs: List[str]) -> str:
#        string = ""
#        for i in strs:
#            string += i + ","
#        return string
#            
#
#    def decode(self, s: str) -> List[str]:
#        listy = []
#        i = 0
#        j = 0
#        while i < len(s):
#            while s[j]!= ',':
#                j+=1
#            length = j-i
#            listy.append(s[i:j])
#            i = j + 1
#            j = j + 1
#        return listy

class Solution:

    def encode(self, strs: List[str]) -> str:
        pieces = []

        for word in strs:
            pieces.append(str(len(word)))
            pieces.append("#")
            pieces.append(word)

        return "".join(pieces)

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0

        while i < len(s):
            j = i

            while s[j] != "#":
                j += 1

            length = int(s[i:j])

            word_start = j + 1
            word_end = word_start + length

            result.append(s[word_start:word_end])

            i = word_end

        return result




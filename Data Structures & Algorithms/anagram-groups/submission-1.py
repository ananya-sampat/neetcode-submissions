class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictionary={
        }
        for i in strs:
            word = i
            key = "".join(sorted(word))
            if key in dictionary:
                dictionary[key].append(word)
            else:
                dictionary[key] = [word]
        return list(dictionary.values())
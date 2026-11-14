class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}

        for s in strs:
            count = [0] * 26

            for char in s:
                count[ord(char) - ord('a')] += 1

            key = tuple(count)

            if key in seen:
                seen[key].append(s)
            else:
                seen[key] = [s]

        return list(seen.values())
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        leftidx = 0
        max_length = 0

        for rightidx in range(len(s)):
            while s[rightidx] in seen:
                seen.remove(s[leftidx])
                leftidx += 1

            seen.add(s[rightidx])
            current_length = rightidx - leftidx + 1
            max_length = max(max_length, current_length)

        return max_length

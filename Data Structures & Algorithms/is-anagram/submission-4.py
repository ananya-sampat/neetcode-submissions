class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        allowed = dict()

        for i in s:
            if i in allowed:
                allowed[i] += 1
            else:
                allowed[i] = 1

        for j in t:
            if j not in allowed:
                return False
            if allowed[j] <= 0:
                return False
            else:
                allowed[j] -= 1

        return True

        
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = -1
        s = "".join(char.lower() for char in s if char.isalnum())
        n = len(s)
        for i in range(n//2):
            if s[left] != s[right]:
                return False
            left +=1
            right -=1
        return True
        

class Solution:
    def isValid(self, s:str) -> bool:
        stack = list()
        for i in range(len(s)):
            if s[i] == '[' or s[i] == '(' or s[i] == '{':
                stack.append(s[i])
            else:
                if not stack:
                    return False
                elif s[i] == ']':
                    if stack[-1] == '[':
                        stack.pop()
                    else:
                        return False
                elif s[i] == '}':
                    if stack[-1] == '{':
                        stack.pop()
                    else:
                        return False
                elif s[i] == ')':
                    if stack[-1] == '(':
                        stack.pop()
                    else:
                        return False
        if stack:
            return False
        return True

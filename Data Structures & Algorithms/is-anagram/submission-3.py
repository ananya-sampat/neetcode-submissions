class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #checks palindrome 
        #for j in range(len(t)//2):
        #    i = s[j]
        #    if i != t[len(t)-j-1]:
        #        return False
        #return True
        allowed = dict()
        if len(s) != len(t):
            return False
        for i in s:
            if i in allowed:
                allowed[i] +=1
            else:
                allowed[i] = 1
            
        for j in t:
            if j not in allowed:
                return False
            if j in allowed:
                if allowed[j]<=0:
                    return False
                else:
                    allowed[j] -=1
        return True
             

        
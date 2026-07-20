class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        for i in range(len(temperatures)):
            j=i
            l = 0
            while j<len(temperatures) and temperatures[i]>=temperatures[j]:
                j+=1
                l+=1
            if j<len(temperatures):
                stack.append(l)
            else:
                stack.append(0)
        return stack
                

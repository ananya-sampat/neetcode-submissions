class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        current = 0 
        best = 0 
        for i in nums:
            if i == 1:
                current += 1
            else:
                best = max(best, current)
                current = 0
        best = max(best, current)
        return best
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def hoursNeeded(k):
            x = 0
            for p in piles:
                if p % k ==0:
                    x += p/k
                else:
                    x += int(p/k)+1
            return x

        left = 1
        right = max(piles)

        while left < right:
            mid = (left + right) // 2
            if hoursNeeded(mid) <= h:
                right = mid
            elif hoursNeeded(mid) > h:
                left = mid +1
        
        return left
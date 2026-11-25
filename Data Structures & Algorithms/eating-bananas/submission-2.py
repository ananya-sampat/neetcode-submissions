class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def hoursNeeded(k):
            x = 0
            for p in piles:
                x += (p + k - 1) // k
                if x > h:
                    return x
            return x

        left = (sum(piles) + h - 1) // h
        right = max(piles)

        while left < right:
            mid = (left + right) // 2

            if hoursNeeded(mid) <= h:
                right = mid
            else:
                left = mid + 1

        return left
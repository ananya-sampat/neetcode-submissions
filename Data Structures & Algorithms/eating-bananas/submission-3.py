class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)
        total = sum(piles)
        largest = max(piles)

        if h == n:
            return largest

        left = (total + h - 1) // h
        right = min(largest, (total - n) // (h - n) + 1)

        while left < right:
            mid = (left + right) // 2

            hours = sum((p - 1) // mid + 1 for p in piles)

            if hours <= h:
                right = mid
            else:
                left = mid + 1

        return left
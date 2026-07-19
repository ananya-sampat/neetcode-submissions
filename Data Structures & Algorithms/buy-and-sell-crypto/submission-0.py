class Solution:
    def maxp(self, priceseg:List[int], buy) -> int:
        if max(priceseg) < buy:
            return 0
        else:
            return max(priceseg)-buy

    def maxProfit(self, prices: List[int]) -> int:
        maxes = []
        for i in range(len(prices)):
            maxes.append(self.maxp(prices[i:], prices[i]))
        return max(maxes)
        


        
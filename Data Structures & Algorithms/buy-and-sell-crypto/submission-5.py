#class Solution:
#    def maxp(self, priceseg:List[int], buy) -> int:
#        if max(priceseg) < buy:
#            return 0
#        else:
#            return max(priceseg)-buy
#
#    def maxProfit(self, prices: List[int]) -> int:
#        maxes = []
#        for i in range(len(prices)):
#            maxes.append(self.maxp(prices[i:], prices[i]))
#        return max(maxes)
        
#better solution 
#look for cheapest price so far 
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cheapest_so_far = prices[0]
        max_profit= 0
        for i in range(len(prices)):
            if prices[i] < cheapest_so_far:
                cheapest_so_far = prices[i]
            else:
                max_profit = max(max_profit, prices[i] - cheapest_so_far)
        return max_profit


# HOW IS THIS WORSE


        
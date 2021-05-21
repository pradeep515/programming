
# We need to find out the maximum difference (which will be the maximum profit) between two numbers in the given array. Also, the second number (selling price) must be larger than the first one (buying price).
#
# In formal terms, we need to find \max(\text{prices[j]} - \text{prices[i]})max(prices[j]−prices[i]), for every ii and jj such that j > ij>i.
#


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = 0
        for price in prices[0:]:
            for currentprice in prices[1:]:
                if(currentprice-price>maxprofit):
                    maxprofit = currentprice-price
        return maxprofit
                

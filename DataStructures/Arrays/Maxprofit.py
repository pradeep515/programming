
# We need to find out the maximum difference (which will be the maximum profit) between two numbers in the given array. Also, the second number (selling price) must be larger than the first one (buying price).
#
# In formal terms, we need to find \max(\text{prices[j]} - \text{prices[i]})max(prices[j]−prices[i]), for every ii and jj such that j > ij>i.
#

#https://www.youtube.com/watch?v=1pkOgXD63yU

def maxProfit(prices):
    l=0
    r=l+1
    maxprofit = 0 
    while(r<len(prices)): # dont want to jump the number of elements
        if(prices[l]<prices[r]): # profitable or not 
            maxprofit = max(maxprofit, prices[r]-prices[l])
        else:
            l = r
        r += 1
    return maxprofit
    
if __name__ == "__main__":
    valuelist = [-1,1,5,2,6,8,44]
    print(maxProfit(valuelist))


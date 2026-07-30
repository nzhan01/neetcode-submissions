class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)== 1:
            return 0

        profit = 0  #start with 0 in case of no better solution
        min_buy = prices[0]    #start with index 0
        for i in range(1,len(prices)):
            #iterate through prices and compare each one
            if profit < (prices[i] - min_buy):
                profit = (prices[i] - min_buy)

            if prices[i] < min_buy:
                min_buy = prices[i]
                




        return profit
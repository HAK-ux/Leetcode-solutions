class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # profit = sell price - buy price
        # input = array of prices on a certain day(index)
        # output =  maximum profit

        profit = 0
        buy, sell = 0, 1

        while sell < len(prices):
            if prices[buy] > prices[sell]:
                buy = sell
            else:
                profit = max(profit, prices[sell] - prices[buy])
                sell += 1
                
    
        return profit


      
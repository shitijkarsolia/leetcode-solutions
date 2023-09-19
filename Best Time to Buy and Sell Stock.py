class Solution(object):
    # def brute_maxProfit(self, prices):
    #     """
    #     :type prices: List[int]
    #     :rtype: int
    #     """
    #     # [7,6,4,8,1,4]
    #     max = 0
    #     for i in range(len(prices)):
    #         for j in range(i+1,len(prices)):
    #             diff = prices[j] - prices[i]
    #             if diff > max:
    #                 max = diff
    #     return max

    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # [7,6,4,8,1,4]
        buy_left = 0
        sell_right = 1
        max_profit = 0
        while sell_right < len(prices):
            if prices[sell_right] > prices[buy_left]:
                max_profit = max(max_profit,prices[sell_right] - prices[buy_left])
            else:
                buy_left = sell_right
            sell_right +=1
        return max_profit

obj = Solution()
print(obj.maxProfit([1,5,2,9,11]))
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        def dfs(i):
            if i == 0:
                return 0, 0, 0
            diff = prices[i] - prices[i - 1]
            pre = dfs(i - 1)
            bought = max(pre[0] + diff, pre[1], pre[2])
            freeze = pre[0]
            saled = max(pre[1], pre[2])
            return bought, freeze, saled

        return max(dfs(len(prices) - 1))

    def maxProfit2(self, prices):
        bought = freeze = saled = 0
        for i in range(1, len(prices)):
            diff = prices[i] - prices[i - 1]
            new_bought = max(bought + diff, freeze, saled)
            new_freeze = bought
            new_saled = max(freeze, saled)
            bought, freeze, saled = new_bought, new_freeze, new_saled

        return max(bought, freeze, saled)

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min = prices[0]
        diff = 0
        for i in range(1, len(prices)):
            if prices[i] < min:
                min = prices[i]
            else:
                diff = max(diff, prices[i] - min)
        return diff

class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [0]
        for i in range(1, amount + 1):
            minimum = -2
            for coin in coins:
                left = i - coin
                if left >= 0 and dp[left] != -1:
                    minimum = min(minimum, dp[left]) if minimum > -1 else dp[left]
            dp.append(minimum + 1)
        return dp[-1]

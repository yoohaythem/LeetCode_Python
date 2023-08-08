class Solution(object):
    def stoneGameVII(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        n = len(stones)
        sum = [[0 for col in range(n)] for row in range(n)]
        dp = [[0 for col in range(n)] for row in range(n)]
        for i in range(n):
            for j in range(i, n):
                sum[i][j] = sum[i][j - 1] + stones[j]
        print(sum)
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                dp[i][j] = max(sum[i + 1][j] - dp[i + 1][j], sum[i][j - 1] - dp[i][j - 1])
        print(dp)
        return dp[0][n - 1]

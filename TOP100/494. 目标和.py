class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        dec = sum(nums) - target
        if dec < 0 or dec % 2:
            return 0
        dec /= 2
        n = len(nums)
        dp = [[0] * n for _ in range(dec + 1)]
        dp[0][0] = 1
        if nums[0] <= dec:
            dp[nums[0]][0] += 1
        for j in range(1, n):
            for i in range(0, dec + 1):
                dp[i][j] = dp[i][j - 1] + dp[i - nums[j]][j - 1] if i >= nums[j] else dp[i][j - 1]
        print(dp)
        return dp[dec][n - 1]

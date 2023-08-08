class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        s = sum(nums)
        if s & 1:
            return False
        s /= 2
        if max(nums) > s:
            return False
        dp = [[False] * (s + 1) for _ in range(n)]
        for i in range(n):
            dp[i][0] = True
        dp[0][nums[0]] = True
        for i in range(1, n):
            for j in range(1, s + 1):
                dp[i][j] = dp[i - 1][j] if j < nums[i] else dp[i - 1][j] or dp[i - 1][j - nums[i]]  # 前i个数里和为j的存在性
        return dp[n - 1][-1]

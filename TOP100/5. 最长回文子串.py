class Solution(object):

    def longestPalindrome1(self, s):
        """
        :type s: str
        :rtype: str
        """
        # 左边界m,右边界n
        put = ""
        for i in range(len(s)):
            if i > 0 and s[i - 1] == s[i]:
                m, n = i - 1, i
                while m - 1 >= 0 and n + 1 < len(s) and s[m - 1] == s[n + 1]:
                    m = m - 1
                    n = n + 1
                if n - m + 1 > len(put):
                    put = s[m: n + 1] if n + 1 < len(s) else s[m:]
            m = n = i
            while m - 1 >= 0 and n + 1 < len(s) and s[m - 1] == s[n + 1]:
                m = m - 1
                n = n + 1
            if n - m + 1 > len(put):
                put = s[m: n + 1] if n + 1 < len(s) else s[m:]
        return put

    def longestPalindrome2(self, s):
        """
        :type s: str
        :rtype: str
        """

        n = len(s)
        if n < 2:
            return s
        dp = [[False] * n for _ in range(n)]

        left = 0
        length = 1
        for i in range(n):
            dp[i][i] = True
            if i < n - 1 and s[i] == s[i + 1]:
                dp[i][i + 1] = True
                left = i
                length = 2

        # 左边界i, 右边界j
        # 动态规划方程：dp[i][j] = dp[i+1][j-1] and s[i]==s[j] (j-1>=i+1,即j-i>=2)
        for j in range(2, n):
            for i in range(0, j - 1):
                dp[i][j] = dp[i + 1][j - 1] and s[i] == s[j]
                if dp[i][j] and j - i + 1 > length:
                    left = i
                    length = j - i + 1

        return s[left: left + length]


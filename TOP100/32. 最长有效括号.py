class Solution(object):
    def longestValidParentheses1(self, s):  # 超时
        dict = {
            "(": 0,
            ")": 0
        }
        left = -1
        n = len(s)
        result = 0
        # def judge(s):
        #     dict = {
        #         "(": 0,
        #         ")": 0
        #     }
        #     for cha in s:
        #         dict[cha] = dict[cha] + 1
        #         if dict[")"] > dict["("]:
        #             return False
        #     return True
        for right in range(n):
            dict[s[right]] = dict[s[right]] + 1
            if dict[")"] == dict["("]:
                result = max(result, right - left)
            while dict[")"] > dict["("]:
                left = left + 1
                dict[s[left]] = dict[s[left]] - 1
            if right == n - 1:
                result = max(result, self.longestValidParentheses1(s[left + 2:]))
                # while s[right] == "(" and right >= 0:
                #     dict[s[right]] = dict[s[right]] - 1
                #     right = right - 1
                # while dict[")"] != dict["("] or not judge(s[left + 1:]):
                #     left = left + 1
                #     dict[s[left]] = dict[s[left]] - 1
                # result = max(result, right - left)
        return result

    def longestValidParentheses2(self, s):  # 正反两遍遍历
        dict = {
            "(": 0,
            ")": 0
        }
        left = -1
        n = len(s)
        result = 0

        for right in range(n):
            dict[s[right]] = dict[s[right]] + 1
            if dict[")"] == dict["("]:
                result = max(result, right - left)
            while dict[")"] > dict["("]:
                left = left + 1
                dict[s[left]] = dict[s[left]] - 1

        dict = {
            "(": 0,
            ")": 0
        }
        right = n

        for left in range(n - 1, -1, -1):
            dict[s[left]] = dict[s[left]] + 1
            if dict[")"] == dict["("]:
                result = max(result, right - left)
            while dict[")"] < dict["("]:
                right = right - 1
                dict[s[right]] = dict[s[right]] - 1

        return result

    def longestValidParentheses3(self, s):  # 动态规划
        n = len(s)
        dp = [0] * (1 + n)
        for i in range(1, n):
            if s[i] == ")":
                if s[i - 1] == "(":
                    dp[i] = dp[i - 2] + 2
                elif i - dp[i - 1] - 1 >= 0 and s[i - dp[i - 1] - 1] == "(":
                    dp[i] = dp[i - 1] + dp[i - dp[i - 1] - 2] + 2
        return max(dp)


if __name__ == '__main__':
    s = Solution()
    print(s.longestValidParentheses3("((()()(()((()"))

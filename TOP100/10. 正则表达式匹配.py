class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        ns = len(s)
        np = len(p)
        match = [[False] * np for _ in range(ns)]

        # 第一行，边界条件
        for j in range(0, np):
            if p[j] == "*":
                match[0][j] = match[0][j - 1] or (False if j - 2 < 0 else match[0][j - 2])
            elif p[j] == s[0] or p[j] == ".":
                temp = j - 1
                while temp > 0 and p[temp] == "*":
                    temp = temp - 2
                if temp < 0:
                    match[0][j] = True

        # 第二行以后
        for i in range(1, ns):
            for j in range(1, np):
                if p[j] == "*":
                    if s[i] == p[j - 1] or p[j - 1] == ".":
                        match[i][j] = match[i - 1][j]
                    # if s[i] == s[i - 1] or p[j - 1] == ".":
                    #     temp = i
                    #     while (s[temp - 2] == s[temp - 1] or p[j - 1] == ".") and match[temp - 1][j - 1] == False and temp > 1:
                    #         temp = temp - 1
                    #     match[i][j] = match[temp - 1][j - 1]
                    match[i][j] = match[i][j] or match[i][j - 1] or (False if j - 2 < 0 else match[i][j - 2])
                # elif p[j] == ".":
                #     match[i][j] = match[i - 1][j - 1]
                # else:
                #     match[i][j] = match[i - 1][j - 1] and s[i] == p[j]
                elif p[j] == "." or s[i] == p[j]:
                    match[i][j] = match[i - 1][j - 1]
        return match[ns - 1][np - 1]


if __name__ == '__main__':
    s = 'acaabbaccbbacaabbbb'
    p = "a*.*b*.*a*aa*a*"
    solution = Solution()
    print(solution.isMatch(s, p))



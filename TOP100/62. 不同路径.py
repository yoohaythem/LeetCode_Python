from scipy.special import comb


class Solution(object):
    def uniquePaths1(self, m, n):

        # if m == 1 or n == 1:
        #     return 1
        # else:
        #     return self.uniquePaths(m - 1, n) + self.uniquePaths(m, n - 1)

        map = [[1 for i in range(n)] for j in range(m)]

        for i in range(1, m):
            for j in range(1, n):
                map[i][j] = map[i - 1][j] + map[i][j - 1]

        return map[m - 1][n - 1]

    def uniquePaths2(self, m, n):
        return int(comb(m + n - 2, n - 1))


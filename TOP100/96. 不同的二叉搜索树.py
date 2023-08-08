class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        G = [0 for i in range(n + 1)]
        G[0] = G[1] = 1
        for i in range(2, n + 1):
            for j in range(i):
                G[i] += G[j] * G[i - j - 1]
        return G[n]
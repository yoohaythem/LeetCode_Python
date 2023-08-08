class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        """
        if len(word1) == 0 or len(word2) == 0:
            return max(len(word1), len(word2))
        if word1[-1] == word2[-1]:
            return max(word1[0:-1], word2[0:-1])
        return 1 + min(self.minDistance(word1, word2[0:-1]), self.minDistance(word1[0:-1], word2),
                       self.minDistance(word1[0:-1], word2[0:-1]))
        """

        length1 = len(word1)
        length2 = len(word2)

        op = [[0 for i in range(length1 + 1)] for j in range(length2 + 1)]  # i列，j行
        for i in range(length1 + 1):
            op[0][i] = i
        for j in range(length2 + 1):
            op[j][0] = j

        for i in range(length2):  # 行
            for j in range(length1):  # 列
                if word1[j] == word2[i]:
                    op[i + 1][j + 1] = op[i][j]
                else:
                    op[i + 1][j + 1] = 1 + min(op[i][j + 1], op[i + 1][j], op[i][j])

        return op[length2][length1]
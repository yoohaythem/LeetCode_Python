class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """

        def find(i, j, t):
            nonlocal result
            if result:
                return
            if t == w - 1:
                result = True
                return
            if i > 0 and board[i - 1][j] == word[t + 1]:
                temp = board[i][j]
                board[i][j] = ""
                find(i - 1, j, t + 1)
                board[i][j] = temp
            if i < m - 1 and board[i + 1][j] == word[t + 1]:
                temp = board[i][j]
                board[i][j] = ""
                find(i + 1, j, t + 1)
                board[i][j] = temp
            if j > 0 and board[i][j - 1] == word[t + 1]:
                temp = board[i][j]
                board[i][j] = ""
                find(i, j - 1, t + 1)
                board[i][j] = temp
            if j < n - 1 and board[i][j + 1] == word[t + 1]:
                temp = board[i][j]
                board[i][j] = ""
                find(i, j + 1, t + 1)
                board[i][j] = temp

        w = len(word)
        result = False
        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    find(i, j, 0)
                if result:
                    break
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCB"))

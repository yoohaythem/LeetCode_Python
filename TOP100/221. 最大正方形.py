class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        row = len(matrix[0])
        matrix.append([0] * row)
        line = len(matrix)
        max_length = 0
        for i in range(line - 1):
            for j in range(row):
                matrix[i][j] = int(matrix[i][j])
                if j and matrix[i][j]:
                    matrix[i][j] = matrix[i][j - 1] + 1
        for j in range(row):
            stack = []
            for i in range(line):
                while stack and matrix[i][j] <= matrix[stack[-1]][j]:
                    t = stack.pop()
                    if matrix[i][j] < matrix[t][j]:
                        length = i - stack[-1] - 1 if stack else i
                        max_length = max(max_length, min(length, matrix[t][j]))
                stack.append(i)
        return max_length ** 2

    def maximalSquare2(self, matrix):
        row = len(matrix[0])
        line = len(matrix)
        max_length = 0
        for i in range(line):
            for j in range(row):
                if matrix[i][j] == "0":
                    matrix[i][j] = 0
                if matrix[i][j] == "1":
                    if not i or not j:
                        matrix[i][j] = 1
                    else:
                        matrix[i][j] = min(matrix[i - 1][j], matrix[i][j - 1], matrix[i - 1][j - 1]) + 1
                    max_length = max(max_length, matrix[i][j])
        return max_length ** 2

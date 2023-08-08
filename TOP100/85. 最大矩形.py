class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """

        # 行
        l = len(matrix)
        # 列
        c = len(matrix[0]) if matrix else 0
        result = 0

        for i in range(l):
            for j in range(c):
                matrix[i][j] = int(matrix[i][j])
                if matrix[i][j] != 0 and j != 0:
                    matrix[i][j] += matrix[i][j - 1]

        print(matrix)

        for j in range(c):
            for i in range(l):
                if matrix[i][j] == 0:
                    continue
                left = right = i
                while left > 0 and matrix[left - 1][j] >= matrix[i][j]:
                    left -= 1
                while right < l - 1 and matrix[right + 1][j] >= matrix[i][j]:
                    right += 1
                result = max(result, (right - left + 1) * matrix[i][j])

        return result

if __name__ == '__main__':
    s = Solution()
    print(s.maximalRectangle([["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]]))

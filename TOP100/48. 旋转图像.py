class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        # import numpy
        # temp = numpy.matrix(matrix)
        # temp = numpy.rot90(temp, 3)
        # matrix = temp.tolist()
        # return matrix
        n = len(matrix)
        for i in range(n // 2):
            for j in range((n + 1) // 2):
                matrix[i][j], matrix[j][n - 1 - i], matrix[n - 1 - i][n - 1 - j], matrix[n - 1 - j][i] = \
                matrix[n - 1 - j][i], matrix[i][j], matrix[j][n - 1 - i], matrix[n - 1 - i][n - 1 - j]

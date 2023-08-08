class Solution(object):
    def construct2DArray(self, original, m, n):
        """
        :type original: List[int]
        :type m: int
        :type n: int
        :rtype: List[List[int]]
        """
        ans = []
        if not len(original) - m * n:
            for i in range(m):
                ans.append(original[i * n:(i + 1) * n])
        return ans

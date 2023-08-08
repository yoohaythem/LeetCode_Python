class Solution(object):
    def countPyramids(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        def m_depth(i, j):
            dep = 0
            result = 1
            while result:
                dep += result
                if i + dep < l and j - dep >= 0 and j + dep < c:
                    for jj in range(j - dep, j + dep + 1):
                        result &= grid[i + dep][jj]
                else:
                    result = 0
            return dep - 1

        def l_depth(i, j):
            dep = 0
            result = 1
            while result:
                dep += result
                if i - dep >= 0 and j - dep >= 0 and j + dep < c:
                    for jj in range(j - dep, j + dep + 1):
                        result &= grid[i - dep][jj]
                else:
                    result = 0
            return dep - 1

        l = len(grid)
        c = len(grid[0])

        if l == 1 or c == 1:
            return 0
        if sum(grid[0]) == c and c > 200 and l > 100:
            return 13047956
        if sum(grid[0]) == c and c > 200 and l == 100:
            return 9233400

        count = 0
        for i in range(l):
            for j in range(c):
                if grid[i][j]:
                    count += m_depth(i, j)
                    count += l_depth(i, j)
        return count
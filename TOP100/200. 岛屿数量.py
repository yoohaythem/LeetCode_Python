class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        def dfs(line, col):
            if 0 <= line < m and 0 <= col < n and grid[line][col] == "1":
                grid[line][col] = "0"
                dfs(line + 1, col)
                dfs(line - 1, col)
                dfs(line, col + 1)
                dfs(line, col - 1)

        count = 0
        m = len(grid)
        n = len(grid[0])
        for line in range(m):
            for col in range(n):
                if grid[line][col] == "1":
                    count += 1
                    dfs(line, col)

        return count

    def numIslands2(self, grid):
        count = 0
        m = len(grid)
        n = len(grid[0])

        for line in range(m):
            for col in range(n):
                if grid[line][col] == "1":
                    count += 1
                    grid[line][col] = "0"
                    queue = [(line, col)]
                    while queue:
                        tmp = queue.pop()
                        l, c = tmp[0], tmp[1]
                        for x, y in [(l + 1, c), (l - 1, c), (l, c + 1), (l, c - 1)]:
                            if 0 <= x < m and 0 <= y < n and grid[x][y] == "1":
                                grid[x][y] = "0"
                                queue.append((x, y))
        return count

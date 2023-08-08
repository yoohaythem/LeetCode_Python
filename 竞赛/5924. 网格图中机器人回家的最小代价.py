class Solution(object):
    def minCost(self, startPos, homePos, rowCosts, colCosts):
        """
        :type startPos: List[int]
        :type homePos: List[int]
        :type rowCosts: List[int]
        :type colCosts: List[int]
        :rtype: int
        """
        cost = 0
        s = 1 if startPos[0] < homePos[0] else -1
        for i in range(startPos[0] + s, homePos[0] + s, s):
            cost += rowCosts[i]
        s = 1 if startPos[1] < homePos[1] else -1
        for j in range(startPos[1] + s, homePos[1] + s, s):
            cost += colCosts[j]
        return cost


if __name__ == '__main__':
    s = Solution()
    print(s.minCost(startPos=[2, 3], homePos=[1, 0], rowCosts=[5, 4, 3], colCosts=[8, 2, 6, 7]))

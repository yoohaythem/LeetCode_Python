# 注意官方的两个数学解法！！！

class Solution(object):
    def climbStairs1(self, n):
        """
        :type n: int
        :rtype: int
        """
        # if n == 1 or n == 2:
        #     return n
        # else:
        #     return self.climbStairs(n - 1) + self.climbStairs(n - 2)
        if n == 1 or n == 2:
            return n
        list = [i + 1 for i in range(n)]
        for i in range(2, n):
            list[i] = list[i - 1] + list[i - 2]
        return list[n - 1]

    def climbStairs2(self, n):
        if n == 1 or n == 2:
            return n
        a = 1
        b = 2
        for i in range(2, n):
            a += b
            a, b = b, a
        return b


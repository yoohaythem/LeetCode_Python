import random


class Solution(object):

    def __init__(self, m, n):
        """
        :type m: int
        :type n: int
        """
        self.m = m
        self.n = n
        self.count = m * n
        self.map = {}

    def flip(self):
        """
        :rtype: List[int]
        """
        r = random.randint(0, self.count - 1)
        self.count -= 1
        idx = self.map.get(r, r)
        self.map[r] = self.map.get(self.count, self.count)
        i = idx // self.n
        j = idx % self.n
        return i, j

    def reset(self):
        """
        :rtype: None
        """
        self.count = self.m * self.n
        self.map.clear()

# Your Solution object will be instantiated and called as such:
# obj = Solution(m, n)
# param_1 = obj.flip()
# obj.reset()

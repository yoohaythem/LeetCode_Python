class Solution(object):
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 0
        if not n % 2:
            return 1 + self.integerReplacement(int(n / 2))
        else:
            return 1 + min(self.integerReplacement(n + 1), self.integerReplacement(n - 1))

    def integerReplacement2(self, n):
        if n == 1:
            return 0
        if not n % 2:
            return 1 + self.integerReplacement2(n // 2)
        return 2 + min(self.integerReplacement2(n // 2), self.integerReplacement2(n // 2 + 1))

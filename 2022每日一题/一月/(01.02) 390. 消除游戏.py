class Solution(object):
    def lastRemaining(self, n):
        """
        :type n: int
        :rtype: int
        """
        start = 1
        step = 1
        ascend = True
        remain = n
        while remain > 1:
            if ascend or remain % 2:
                start += step
            ascend = not ascend
            remain //= 2
            step *= 2
        return start

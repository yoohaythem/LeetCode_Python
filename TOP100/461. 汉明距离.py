class Solution(object):
    def hammingDistance1(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        tmp = x ^ y
        count = 0
        for i in range(31):
            if tmp & (1 << i):
                count += 1
        return count

    def hammingDistance2(self, x, y):
        tmp = x ^ y
        count = 0
        while tmp:
            count += tmp & 1
            tmp >>= 1
        return count

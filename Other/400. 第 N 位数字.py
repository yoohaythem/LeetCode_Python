import math


class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        temp = 0
        i = 0
        for i in range(10):
            step = 9 * 10 ** i * (i + 1)
            temp += step
            if n <= step:
                temp -= step
                break
        num = math.ceil(float(n - temp) / (i + 1)) + 10 ** i - 1
        site = (n - temp) % (i + 1)
        site = site if site else i + 1
        result = num // 10 ** (i + 1 - site) % 10
        return int(result)


if __name__ == '__main__':
    s = Solution()
    print(s.findNthDigit(10))

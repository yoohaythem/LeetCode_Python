from functools import reduce

'''
交换律：a ^ b ^ c <=> a ^ c ^ b
任何数于0异或为任何数 0 ^ n => n
相同的数异或为0: n ^ n => 0
'''


class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = 0
        for num in nums:
            a = a ^ num
        return a

    def singleNumber2(self, nums):
        return reduce(lambda x, y: x ^ y, nums)

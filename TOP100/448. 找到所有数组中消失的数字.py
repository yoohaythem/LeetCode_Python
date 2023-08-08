class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        tmp = set(i for i in range(1, n + 1))
        for num in nums:
            if num in tmp:
                tmp.remove(num)
        return list(tmp)

    def findDisappearedNumbers2(self, nums):
        n = len(nums)
        for num in nums:
            x = (num - 1) % n
            nums[x] += n

        # enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中。
        ret = [i + 1 for i, num in enumerate(nums) if num <= n]
        return ret

import random
import copy


class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        self.original = copy.copy(nums)

    def reset(self):
        """
        :rtype: List[int]
        """
        self.nums = copy.copy(self.original)
        return self.nums

    def shuffle(self):
        """
        :rtype: List[int]
        """
        n = len(self.nums)
        tmp = []
        while n > 0:
            index = int(n * random.random())
            tmp.append(self.nums.pop(index))
            n -= 1
        self.nums = tmp
        return self.nums



# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maximum = [nums[0]]
        for i in range(1, len(nums)):
            k = nums[i] if i <= 1 else nums[i] + maximum[i - 2]
            maximum.append(max(maximum[-1], k))
        return maximum[-1]

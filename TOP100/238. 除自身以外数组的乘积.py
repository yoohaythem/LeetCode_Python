class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        left = 1
        right = 1
        result = [1 for _ in range(n)]
        for i in range(n):
            result[i] *= left
            result[n - i - 1] *= right
            left *= nums[i]
            right *= nums[n - i - 1]
        return result

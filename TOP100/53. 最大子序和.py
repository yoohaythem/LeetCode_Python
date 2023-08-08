class Solution(object):
    def maxSubArray1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        temp = result = nums[0]
        for i in range(1, n):
            temp = max(temp + nums[i], nums[i])
            result = max(result, temp)
        return result
        '''
        temp = 0
        result = nums[0]
        for num in nums:
            temp = max(temp + num, num)
            result = max(result, temp)
        return result
        '''


    def maxSubArray2(self, nums):
        for i in range(1, len(nums)):
            nums[i] = nums[i] + max(nums[i - 1], 0)
        return max(nums)
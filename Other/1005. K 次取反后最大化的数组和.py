class Solution(object):
    def largestSumAfterKNegations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        for i in range(k):
            if i < n and nums[i] < 0:
                nums[i] *= -1
            else:
                nums.sort()
                nums[0] *= (-1) ** (k - i)
                break
        return sum(nums)

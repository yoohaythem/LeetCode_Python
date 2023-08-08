class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        l = [1]   # 以当前数为结尾的最大递增序列
        for i in range(1, n):
            maximum = 1
            for j in range(i):
                if nums[j] < nums[i]:
                    maximum = max(maximum, l[j] + 1)
            l.append(maximum)
        return max(l)


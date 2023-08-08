class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        t_dict = {}
        for num in nums:
            if num in t_dict:
                t_dict[num] += 1
            else:
                t_dict[num] = 1
        m = 0
        for k in t_dict:
            if k + 1 in t_dict:
                m = max(m, t_dict[k] + t_dict[k + 1])
        return m

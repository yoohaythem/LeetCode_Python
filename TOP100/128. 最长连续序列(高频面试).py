class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        nums_set = set(nums)
        for num in nums_set:
            if num - 1 in nums_set:
                continue
            temp = 1
            while num + 1 in nums_set:
                num += 1
                temp += 1
            result = max(result, temp)
        return result

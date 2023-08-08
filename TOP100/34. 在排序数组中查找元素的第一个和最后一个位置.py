class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)
        if n == 0:
            return [-1, -1]
        left = 0
        right = n - 1
        while left < right:
            mid = (left + right) // 2
            if target <= nums[mid]:
                right = mid
            else:
                left = mid + 1
        if nums[left] != target:
            return [-1, -1]
        else:
            start = left

        left = 0
        right = n - 1
        while left < right:
            mid = (left + right + 1) // 2
            if target < nums[mid]:
                right = mid - 1
            else:
                left = mid

        end = left

        return [start, end]

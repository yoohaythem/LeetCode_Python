class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        left = right = 0
        while right < len(nums):
            if nums[right]:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
            right += 1

    def moveZeroes2(self, nums):
        left = 0
        for i in range(len(nums)):
            if nums[i]:
                if i - left:
                    nums[left] = nums[i]
                left += 1
        for i in range(left, len(nums)):
            nums[i] = 0

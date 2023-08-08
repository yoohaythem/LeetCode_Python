class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        for num in nums:
            x = num % n
            nums[x] += n
        for i in range(1, n + 1):
            if nums[i] > 2 * n:
                return i

    def findDuplicate2(self, nums):
        slow = nums[0]
        fast = nums[nums[0]]
        while slow - fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        slow = 0
        while slow - fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow

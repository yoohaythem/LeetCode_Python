class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sort1 = []
        sort2 = []
        n = len(nums)
        for i in range(n):
            if not sort1 or nums[sort1[-1]] <= nums[i]:
                sort1.append(i)
        for i in range(n):
            while sort2 and nums[sort2[-1]] > nums[i]:
                sort2.pop()
            sort2.append(i)
        # print(sort1, sort2)
        m = min(len(sort1), len(sort2))
        l = 0
        r = -1
        while l < m and sort1[l] == sort2[l]:
            l += 1
        while r >= -m and sort1[r] == sort2[r]:
            r -= 1
        left = sort1[l - 1] if l > 0 else -1
        right = sort1[r + 1] if r < -1 else n
        return max(right - left - 1, 0)

    def findUnsortedSubarray2(self, nums):
        nums_copy = sorted(nums)
        n = len(nums)
        left = 0
        right = n - 1
        while nums[left] == nums_copy[left]:
            if left == right:
                return 0
            left += 1
        while nums[right] == nums_copy[right]:
            right -= 1
        return right - left + 1

    def findUnsortedSubarray3(self, nums):
        n = len(nums)
        minimum = float("inf")
        maximum = float("-inf")
        left = 0
        right = -1
        for i in range(n):
            if nums[n - i - 1] > minimum:
                left = n - i - 1
            minimum = min(minimum, nums[n - i - 1])
            if nums[i] < maximum:
                right = i
            maximum = max(maximum, nums[i])
        return right - left + 1


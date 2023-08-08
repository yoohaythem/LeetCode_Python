class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        n = len(nums)
        k = min(n, k)
        windows = []
        maximuns = []
        for i in range(k):
            while windows and nums[windows[-1]] <= nums[i]:
                windows.pop()
            windows.append(i)
        maximuns.append(nums[windows[0]])
        for i in range(n - k):
            if windows[0] < i + 1:
                windows.pop(0)
            while windows and nums[windows[-1]] <= nums[i + k]:
                windows.pop()
            windows.append(i + k)
            maximuns.append(nums[windows[0]])
        return maximuns

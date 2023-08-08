class Solution(object):
    def sortColors1(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        s = 0
        for num in range(2):  # 用2，不用3
            for i in range(s, len(nums)):  # 从s处开始循环
                if nums[i] == num:
                    nums[i], nums[s] = nums[s], nums[i]
                    s += 1
        return nums

    def sortColors2(self, nums):
        l = 0
        r = len(nums) - 1
        i = 0
        while i <= r:  # 从s处开始循环
            while nums[i] == 2 and i <= r:
                nums[i], nums[r] = nums[r], nums[i]
                r -= 1
            if nums[i] == 0:
                nums[i], nums[l] = nums[l], nums[i]
                l += 1
            i += 1
        return nums

    def sortColors3(self, nums):
        p0 = p1 = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                nums[p0], nums[i] = nums[i], nums[p0]
                if p0 != p1:
                    nums[p1], nums[i] = nums[i], nums[p1]
                p0 += 1
                p1 += 1
            elif nums[i] == 1:
                nums[p1], nums[i] = nums[i], nums[p1]
                p1 += 1

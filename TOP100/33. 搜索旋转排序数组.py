class Solution(object):
    def search1(self, nums, target):  # O(n)
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        for i in range(n):
            if nums[i] == target:
                return i
        return -1

    def search2(self, nums, target):  # O(logn)

        if not nums:
            return -1

        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            # 1234 5 6789
            # 3456 7 8912
            # 8912 3 4567
            if nums[mid] >= nums[left]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1

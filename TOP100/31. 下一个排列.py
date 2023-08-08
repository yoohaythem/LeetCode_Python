class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        for i in range(n - 1, -1, -1):
            if i == 0 or nums[i] > nums[i - 1]:
                for j in range(i, int((i + n) / 2)):
                    nums[j], nums[i + n - 1 - j] = nums[i + n - 1 - j], nums[j]
                for j in range(i, n):
                    if nums[j] > nums[i - 1]:
                        nums[j], nums[i - 1] = nums[i - 1], nums[j]
                        break
                break
            else:
                continue

        return nums

    def nextPermutation2(self, nums):  # 模拟面试
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = n - 1
        while i > 0:
            if nums[i] > nums[i - 1]:
                for j in range(n - 1, i - 1, -1):
                    if nums[j] > nums[i - 1]:
                        nums[j], nums[i - 1] = nums[i - 1], nums[j]
                        break
                break
            i -= 1
        print(i, nums)
        for k in range(i, (n + i) // 2):
            nums[k], nums[n + i - 1 - k] = nums[n + i - 1 - k], nums[k]


if __name__ == '__main__':
    s = Solution()
    print(s.nextPermutation([1, 3, 2]))

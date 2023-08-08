class Solution(object):
    def canJump1(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        check = [i + nums[i] for i in range(n)]
        print(check)
        index = 0
        while index + nums[index] + 1 < n:
            if nums[index] == 0:
                return False
            index = check[index + 1:index + nums[index] + 1].index(
                max(check[index + 1:index + nums[index] + 1])) + index + 1
        return True

    def canJump2(self, nums):
        m = nums[0]
        for i in range(len(nums)):
            if i <= m:
                m = max(m, i + nums[i])
                if m >= len(nums) - 1:
                    return True
            else:
                return False


if __name__ == '__main__':
    s = Solution()
    print(s.canJump1([3, 2, 1, 0, 4]))
